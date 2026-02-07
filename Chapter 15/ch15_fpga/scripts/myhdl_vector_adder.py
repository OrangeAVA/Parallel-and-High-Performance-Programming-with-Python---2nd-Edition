from myhdl import block, always_seq, always, Signal, ResetSignal, intbv, delay, instance, StopSimulation

@block
def vector_adder(clk, reset, a, b, result):
    """ 4-element parallel adder (8 bits each). Updates on each rising edge. """
    @always_seq(clk.posedge, reset=reset)
    def logic():
        for i in range(len(a)):
            # result has +1 bit to capture overflow
            result[i].next = a[i] + b[i]
    return logic

@block
def testbench():
    clk = Signal(0)
    reset = ResetSignal(0, active=1, isasync=False)

    N = 4
    W = 8

    a = [Signal(intbv(0)[W:]) for _ in range(N)]
    b = [Signal(intbv(0)[W:]) for _ in range(N)]
    result = [Signal(intbv(0)[W+1:]) for _ in range(N)]  # +1 for overflow

    dut = vector_adder(clk, reset, a, b, result)

    @always(delay(5))
    def clk_gen():
        clk.next = not clk

    @instance
    def stim():
        print("Start simulation")
        reset.next = 1
        yield clk.posedge
        reset.next = 0

        tests = [
            ([10, 20, 30, 40], [1, 2, 3, 4]),
            ([5, 15, 25, 35], [10, 20, 30, 40]),
            ([255, 128, 64, 32], [1, 2, 3, 4]),  # overflow on first
        ]

        for cycle, (va, vb) in enumerate(tests, start=1):
            for i in range(N):
                a[i].next = va[i]
                b[i].next = vb[i]
            yield clk.posedge
            print(f"Cycle {cycle}: A={va}, B={vb}, Result={[int(r) for r in result]}")

        raise StopSimulation

    return dut, clk_gen, stim

if __name__ == "__main__":
    tb = testbench()
    tb.run_sim()
