import os
import uvicorn

port = int(os.environ.get("PORT", 8080))  # <-- usa el que viene del entorno
print(f"🚀 Arrancando en puerto: {port}")

uvicorn.run("main:app", host="0.0.0.0", port=port)
