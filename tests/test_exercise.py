import pytest
import src.exercise

def test_exercise():
    input_values = ["Good thank you!","Well, there's really nothing to tell."]
    input_values_stored = ["Good thank you!","Well, there's really nothing to tell."]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[2],output[4]] == ["Greetings! How are you doing?","Oh, how interesting. Tell me more!","Thanks for sharing!"]
    assert [output[1],output[3]] == [input_values_stored[0],input_values_stored[1]]
