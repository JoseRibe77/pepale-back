import os, uvicorn

print("🚀 ENTRYPOINT INICIADO")
port = int(os.getenv("PORT", "8000"))
print(f"🎯 Escuchando en puerto {port}")
uvicorn.run("main:app", host="0.0.0.0", port=port)
