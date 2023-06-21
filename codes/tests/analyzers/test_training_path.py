import networkx as nx
import plotly.graph_objects as pg

import codes


def test_plot_path():
    graph = nx.gnm_random_graph(n=10, m=40)
    qaoa = codes.examples.qaoa_maxcut.QAOACircuitMaxCut(graph, p=1)
    circuit = codes.interface.circuit.CircuitDescriptor(
        qaoa.qaoa_circuit, qaoa.params, qaoa.qaoa_cost
    )
    trainer = codes.simulators.pqc_trainer.PQCSimulatedTrainer(circuit)
    metric = codes.examples.qaoa_maxcut.MaxCutMetric(graph)

    plot = codes.analyzers.loss_landscape.LossLandscapePlotter(trainer, metric, dim=2)
    trackers = codes.interface.metas.AnalyzerList(
        codes.analyzers.training_path.LossLandscapePathPlotter(plot),
        codes.analyzers.training_path.OptimizationPathPlotter(mode="tSNE"),
    )
    for _i in range(5):
        trainer.train(loggers=trackers)
        trackers.next()
    fig_loss_traversal = trackers[0].plot()
    fig_training_trace = trackers[1].plot()

    assert isinstance(
        fig_loss_traversal, pg.Figure
    ), "Plot of incorrect type was returned"
    assert isinstance(
        fig_training_trace, pg.Figure
    ), "Plot of incorrect type was returned"
