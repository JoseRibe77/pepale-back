# Pepale Backend

Este backend incluye:
- Registro de ventas con base de datos Supabase (via SQLAlchemy)
- Envío de correos a cada venta
- Rutas para auth y productos

## Despliegue
1. Configura Railway con este código.
2. Crea tabla 'ventas' en Supabase.
3. Define variables de entorno: `DATABASE_URL`, `SMTP_USER`, `SMTP_PASS`
