import codes


def test_trainer():
    qaoa_maxcut = codes.examples.qaoa_maxcut.QAOACircuitMaxCut()
    circuit_descriptor = codes.interface.circuit.CircuitDescriptor(
        circuit=qaoa_maxcut.qaoa_circuit,
        params=qaoa_maxcut.params,
        cost_function=qaoa_maxcut.qaoa_cost,
    )
    pqc_trainer = codes.simulators.pqc_trainer.PQCSimulatedTrainer(
        circuit=circuit_descriptor
    )
    pqc_trainer.train()


def test_evaluation():
    qaoa_maxcut = codes.examples.qaoa_maxcut.QAOACircuitMaxCut()
    circuit_descriptor = codes.interface.circuit.CircuitDescriptor(
        circuit=qaoa_maxcut.qaoa_circuit,
        params=qaoa_maxcut.params,
        cost_function=qaoa_maxcut.qaoa_cost,
    )
    pqc_trainer = codes.simulators.pqc_trainer.PQCSimulatedTrainer(
        circuit=circuit_descriptor
    )
    logger = codes.interface.metas.AnalyzerList(
        codes.analyzers.training_path.OptimizationPathPlotter()
    )
    loss_1 = pqc_trainer.evaluate(1000)
    pqc_trainer.train(10000, loggers=logger)
    loss_2 = pqc_trainer.evaluate(1000)
    assert loss_1 >= loss_2, "Training worsened the output accuracy."
