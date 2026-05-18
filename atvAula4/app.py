from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/profissional')
def profissional():
    dados = {
        "nome": "FELIPE MATOS CARVALHO",
        "idade": "17 anos",
        "endereco": "Rua Içana, 231, Apto 202, Nova Suíça. Belo Horizonte, Minas Gerais.",
        "telefone": "(31) 982110718",
        "email": "matoscarvalhofelp@gmail.com",
        "formacao": "Cursando 3º ano do Ensino Médio e Técnico em Informática, turno manhã - Colégio Cotemig Barroca.",
        "experiencia": {
            "titulo": "Mart Minas | Jovem Aprendiz de TI (Março/2026 – Atual)",
            "descricao": "Início na Infraestrutura com manutenção de PCs, configuração de redes, domínio Windows e sistema TOTVS. Desde abril, atuo no setor de Desenvolvimento focado em melhorias de sistemas e apoio em pequenos projetos internos."
        },
        "hard_skills": [
            "Manutenção hardware e software",
            "Conhecimento intermediário em HTML, CSS, C#, MYSQL e PHP",
            "Conhecimento iniciante em JavaScript, Python e Inglês"
        ],
        "soft_skills": [
            "Facilidade em aprendizado",
            "Conhecimento de ferramentas do Google",
            "Trabalho em equipe",
            "Resolução de problemas",
            "Sociável"
        ],
        "objetivos": [
            "Aprimorar o conhecimento na utilização de sistemas operacionais;",
            "Aperfeiçoar habilidades com aplicativos e em linguagens de programação;",
            "Busco qualificação na área de informática para aperfeiçoamento do curso técnico."
        ],
        "certificacoes": [
            "Emblemas Cisco Networking Academy (Python Essentials 1, Computer Hardware Basics, Introduction to IoT, entre outros)"
        ]
    }
    
    return render_template("profissional.html", dados=dados) 
@app.route('/expectativa')
def expectativa():
    return render_template("expectativa.html")

if __name__ == '__main__':
    app.run(debug=True)