import google.generativeai as genai
import PIL.Image
import os
from fpdf import FPDF
from datetime import datetime

# --- CONFIGURAÇÃO MANUAL (PROTOCOLO CAVI) ---
CHAVE = "AIzaSyB-VcrWMP-F9AqEp48lwVTh-CgzKagq-x8"
genai.configure(api_key=CHAVE)

# Aqui está o segredo: forçamos a versão 1.5 Flash de forma direta
model = genai.GenerativeModel('gemini-1.5-flash')

print("🚀 MOTOR GEMINI INICIADO NO CENTRO MÉDICO CAVI")

# Dados do Paciente [cite: 2026-02-19]
nome_p = input("👉 Nome do Paciente: ").upper()
idade_p = input("👉 Idade: ")
foto_nome = input("👉 Nome da Foto do Exame: ")

if not os.path.exists(foto_nome):
    print("❌ Erro: Foto não encontrada na pasta!")
else:
    try:
        print("📸 O Gemini está a analisar a imagem...")
        img = PIL.Image.open(foto_nome)
        
        # O comando que tu queres que a IA execute
        prompt = "Analise este hemograma. Extraia os valores de Hemoglobina, Hematócrito, Leucócitos e Plaquetas."
        
        # LIGAÇÃO DIRETA
        response = model.generate_content([prompt, img])
        laudo_texto = response.text
        
        print("\n✅ SUCESSO! A IA LEU O EXAME.")
        print("-" * 30)
        print(laudo_texto)
        print("-" * 30)

        # AGORA GERAMOS O TEU PDF COM DESIGN PREMIUM [cite: 2026-02-19]
        pdf = FPDF()
        pdf.add_page()
        
        # Barra Azul de Topo (O teu estilo SocialMed)
        pdf.set_fill_color(0, 51, 102)
        pdf.rect(10, 10, 190, 30, 'F')
        pdf.set_xy(15, 15)
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 10, "CENTRO MÉDICO CAVI - LAUDO IA", 0, 1)
        pdf.set_font("Arial", '', 10)
        pdf.cell(0, 5, f"PACIENTE: {nome_p} | IDADE: {idade_p}", 0, 1)

        # Corpo do Laudo
        pdf.ln(25)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "RESULTADOS ANALISADOS:", ln=True)
        pdf.set_font("Arial", '', 11)
        pdf.multi_cell(0, 7, laudo_texto.replace("**", ""))

        pdf.output(f"LAUDO_GEMINI_{nome_p}.pdf")
        print(f"\n📄 PDF GERADO: LAUDO_GEMINI_{nome_p}.pdf")

    except Exception as e:
        # Se der erro, o código vai dizer exatamente porquê
        print(f"⚠️ Erro técnico no Gemini: {e}")
