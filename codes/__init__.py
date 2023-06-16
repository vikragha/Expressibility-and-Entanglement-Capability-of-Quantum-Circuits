"""The qLEET Package for visualizing quantum circuit behavior"""
import os

import codes.examples
import codes.analyzers
import codes.simulators
import codes.interface

from codes.interface.metas import AnalyzerList
from codes.interface.circuit import CircuitDescriptor

from codes.analyzers.training_path import OptimizationPathPlotter
from codes.analyzers.loss_landscape import LossLandscapePlotter
from codes.analyzers.expressibility import Expressibility
from codes.analyzers.entanglement import EntanglementCapability
from codes.analyzers.entanglement_spectrum import EntanglementSpectrum
from codes.analyzers.histogram import ParameterHistograms

from codes.simulators.circuit_simulators import CircuitSimulator
from codes.simulators.pqc_trainer import PQCSimulatedTrainer

from codes.examples.qaoa_maxcut import QAOACircuitMaxCut, MaxCutMetric
from codes._version import __version__

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
