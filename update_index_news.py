import re

index_path = 'site-siqueira-campos-jr-35/index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern matching section 6 news
pattern = r'<!-- 6\. NOT[^\n]+-->[\s\S]*?</section>'
match = re.search(pattern, html)
if not match:
    print('Error: Pattern not found!')
    exit(1)

new_section = '''<!-- 6. NOTÍCIAS EM DESTAQUE (MODELO EDITORIAL IDÊNTICO AO FLÁVIO BOLSONARO) -->
      <section class="news-home-section" id="noticias" style="padding: 70px 0; background: #ffffff;">
        <div class="container">
          
          <!-- CABEÇALHO DA SEÇÃO: | NOTÍCIAS ─────────────── VER TODAS > -->
          <div class="news-editorial-header">
            <h2 class="news-editorial-title">NOTÍCIAS</h2>
            <div class="news-editorial-line" aria-hidden="true"></div>
            <a href="noticias.html" class="news-editorial-link">VER TODAS <span>&gt;</span></a>
          </div>

          <!-- GRID EDITORIAL DE 2 COLUNAS (DESTAQUE + EM PAUTA) -->
          <div class="news-editorial-grid">
            
            <!-- COLUNA ESQUERDA: SUPER HERO + GRID DUPLO -->
            <div class="news-editorial-main">
              
              <!-- 1. Super Destaque Principal (Hero 16:9) -->
              <a href="noticia.html" class="news-hero-card reveal">
                <div class="news-hero-media">
                  <img src="./assets/news/thumb-destaque-chapa-35.webp" alt="Siqueira Campos Jr assume candidatura ao Governo do Tocantins pelo Democrata 35 com Capitão Osmar como vice" />
                  <span class="news-hero-badge">Eleições 2026</span>
                </div>
                <h3 class="news-hero-title">Siqueira Campos Jr assume candidatura ao Governo do Tocantins pelo Democrata 35 com Capitão Osmar como vice</h3>
                <span class="news-action-link">LEIA MAIS</span>
              </a>

              <!-- 2. Grid Duplo Inferior (2 Cards Lado a Lado) -->
              <div class="news-sub-grid">
                
                <a href="noticia.html#seguranca" class="news-sub-card reveal">
                  <div class="news-sub-media">
                    <img src="./assets/news/thumb-seguranca-capitao-osmar.webp" alt="Capitão Osmar apresenta plano integrado de segurança e inteligência nos 139 municípios" loading="lazy" />
                    <span class="news-sub-badge">Segurança</span>
                  </div>
                  <h4 class="news-sub-title">Capitão Osmar apresenta plano integrado de segurança e inteligência nos 139 municípios</h4>
                  <span class="news-action-link">LEIA MAIS</span>
                </a>
              
                <a href="noticia.html#agro" class="news-sub-card reveal">
                  <div class="news-sub-media">
                    <img src="./assets/news/thumb-agro-100mil-familias.webp" alt="Agro Tocantins: Meta de 100 mil famílias produtivas com apoio à agroindústria" loading="lazy" />
                    <span class="news-sub-badge">Agronegócio</span>
                  </div>
                  <h4 class="news-sub-title">Agro Tocantins: Meta de 100 mil famílias produtivas com apoio à agroindústria</h4>
                  <span class="news-action-link">LEIA MAIS</span>
                </a>
              
              </div>

            </div>

            <!-- COLUNA DIREITA: SIDEBAR "EM PAUTA" -->
            <aside class="news-editorial-sidebar">
              <div class="news-sidebar-card reveal">
                <div class="news-sidebar-header">
                  <h3 class="news-sidebar-title">EM PAUTA</h3>
                </div>

                <div class="news-pauta-list">
                  
                  <a href="noticia.html#modal" class="news-pauta-item">
                    <span class="news-pauta-cat">Infraestrutura</span>
                    <h4 class="news-pauta-title">Tocantins Modal: Integração da Ferrovia Norte-Sul e Hidrovia Tocantins-Araguaia</h4>
                    <span class="news-pauta-date" data-nosnippet>8 de setembro de 2026</span>
                  </a>
                
                  <a href="noticia.html#saude" class="news-pauta-item">
                    <span class="news-pauta-cat">Saúde</span>
                    <h4 class="news-pauta-title">Saúde Perto de Casa: Fim do sofrimento na ambulância e fortalecimento regional</h4>
                    <span class="news-pauta-date" data-nosnippet>7 de setembro de 2026</span>
                  </a>
                
                  <a href="noticia.html#tecnologia" class="news-pauta-item">
                    <span class="news-pauta-cat">Educação &amp; Inovação</span>
                    <h4 class="news-pauta-title">Tocantins Vale da Tecnologia: UNITINS na formação e atração de empresas inovadoras</h4>
                    <span class="news-pauta-date" data-nosnippet>6 de setembro de 2026</span>
                  </a>
                
                </div>

                <a href="noticias.html" class="news-sidebar-btn">
                  VER MAIS NOTÍCIAS <span>&gt;</span>
                </a>
              </div>
            </aside>

          </div>

        </div>
      </section>'''

html_updated = html[:match.start()] + new_section + html[match.end():]

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html_updated)

print("Successfully replaced news section in index.html!")
