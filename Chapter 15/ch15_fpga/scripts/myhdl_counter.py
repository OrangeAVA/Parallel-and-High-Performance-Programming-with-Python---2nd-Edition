from myhdl import block, always_seq, always, Signal, ResetSignal, intbv, delay, instance, StopSimulation

@block
def counter(clk, reset, count):
    """ 4-bit counter with synchronous reset """
    @always_seq(clk.posedge, reset=reset)
    def logic():
        if reset:
            count.next = 0
        else:
            count.next = (count + 1) % 16  # wrap at 4 bits
    return logic

@block
def testbench():
    clk = Signal(0)
    reset = ResetSignal(0, active=1, isasync=False)
    count = Signal(intbv(0, min=0, max=16))

    dut = counter(clk, reset, count)

    @always(delay(5))  # 10 time-unit period
    def clk_gen():
        clk.next = not clk

    @instance
    def stim():
        print("Start simulation")
        # Apply reset for 1 rising edge
        reset.next = 1
        yield clk.posedge
        reset.next = 0

        # 20 clock cycles
        for i in range(20):
            yield clk.posedge
            print(f"Clock cycle {i+1}, Count: {int(count)}")

        raise StopSimulation

    return dut, clk_gen, stim

if __name__ == "__main__":
    tb = testbench()
    tb.run_sim()
