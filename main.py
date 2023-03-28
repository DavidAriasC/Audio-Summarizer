import openai

openai.api_key = "YOUR_KEY"

def summarize_audio(audio_file, max_length=60):
    # First, transcribe the audio using Whisper API
    audio_file = open(audio_file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)

    # Then, use ChatGPT to generate a summary of the transcription
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following text: {transcript}",
        temperature=0.5,
        max_tokens=max_length,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    summary = response['choices'][0]['text']

    return summary
