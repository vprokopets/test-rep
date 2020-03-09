import time
from time_based import TimeBased

class TestStopConditions:

    def test_0_answer(self):
        # Test 0 is used for test structure correctness check
        # It repeats finished experiment conditions (Triggered Default and Guaranteed SC only)
        # Here and below expected_results means will SC block stop BRISE or not
        expected_results = False

        decision = self.get_actual_results()
        assert decision == expected_results

    def get_actual_results(self):

        sc = TimeBased()
        time.sleep(2)
        return sc.check_state()
        
