import whisper as whr

model = whr.load_model("small")

result = model.transcribe("felvetel.m4a", language="hu")

print(result)