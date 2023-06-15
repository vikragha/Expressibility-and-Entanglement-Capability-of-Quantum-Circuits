import typing
import warnings

import tensorflow as tf

from ..interface.metas import AnalyzerList
from ..interface.circuit import CircuitDescriptor

warnings.filterwarnings("ignore")


class PQCSimulatedTrainer:
    """A class to train parametrized Quantum Circuits in Tensorflow Quantum
    Uses gradient descent over the provided parameters, using the TFQ Adjoint differentiator.
    """

    def __init__(self, circuit: CircuitDescriptor):
        """Constructs a PQC Trainer object to train the circuit.
        :type circuit: CircuitDescriptor
        :param circuit: The circuit object to train on the loss function
        """
        self.optimizer = tf.keras.optimizers.Adam(lr=0.01)
        self.model = tf.keras.models.Sequential([circuit.qiskit_circuit])
        self.circuit = circuit

    def train(
        self, n_samples=100, loggers: typing.Optional[AnalyzerList] = None
    ) -> tf.keras.Model:
        """Trains the parameter of the circuit to minimize the loss.
        :type n_samples: int
        :param n_samples: Number of samples to train the circuit over
        :type loggers: `AnalyzerList`
        :param loggers: The AnalyzerList that tracks the training of the model
        :returns: The trained model
        :rtype: tf.keras.Model
        """
        dummy_input = tf.zeros((1, self.circuit.num_qubits))
        total_error = 0.0
        with tqdm.trange(n_samples) as iterator:
            iterator.set_description("QAOA Optimization Loop")
            for step in iterator:
                with tf.GradientTape() as tape:
                    error = self.model(dummy_input)
                grads = tape.gradient(error, self.model.trainable_variables)
                self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))
                error = error.numpy()
                if loggers is not None:
                    loggers.log(self, error)
                total_error += error
                iterator.set_postfix(error=total_error / (step + 1))
        return self.model

    def evaluate(self, n_samples: int = 1000) -> float:
        """Evaluates the Parametrized Quantum Circuit.
        :type n_samples: int
        :param n_samples: The number of samples to evaluate the circuit over
        :returns: The average loss of the circuit over all the samples
        :rtype: float
        """
        dummy_input = tf.zeros((1, self.circuit.num_qubits))
        total_error = 0.0
        with tqdm.trange(n_samples) as iterator:
            iterator.set_description("QAOA Evaluation Loop")
            for step in iterator:
                error = self.model(dummy_input)
                error = error.numpy()
                total_error += error
                iterator.set_postfix(error=total_error / (step + 1))
        return total_error / n_samples
