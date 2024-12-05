def test_convert():
    from pathlib import Path
    import soundfile as sf  # for reading audio
    import dfpwm

    data, sample_rate = sf.read('./examples/out1.mp3')  # read audio

    # If sample rate is not 48000, may get strange result
    # use `dfpwm.resample(...)` to resample
    if sample_rate != dfpwm.SAMPLE_RATE:
        raise ValueError(f"{sample_rate} != {dfpwm.SAMPLE_RATE}")

    if len(data.shape) != 0 and data.shape[1] > 1:
        data = data[:, 0]  # get channel 0

    dfpwm = dfpwm.compressor(data)  # convert

    Path('out.dfpwm').write_bytes(dfpwm)  # write result to file
