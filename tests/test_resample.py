
import pytest
import importlib

@pytest.mark.skipif(
    not importlib.util.find_spec("librosa"), reason="requires librosa"
)
def test_resample():
    from io import BytesIO
    from pathlib import Path
    import soundfile as sf  # for reading audio
    import dfpwm
    assert dfpwm.SAMPLE_RATE, 48000 # make lint happy

    by = Path('./examples/out1.mp3').read_bytes()
    resampled_data1 = dfpwm.resample_from_file(BytesIO(by))

    data, sample_rate = sf.read('./examples/out1.mp3')
    resampled_data2 = dfpwm.resample(data, sample_rate)
    assert resampled_data1 == resampled_data2
