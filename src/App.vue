<script setup>
import { ref } from 'vue'

const navItems = [
  { href: '#nosotros', label: 'Nosotros' },
  { href: '#maleku', label: 'Maleku' },
  { href: '#idioma', label: 'Idioma' },
  { href: '#tradiciones', label: 'Tradiciones' },
  { href: '#proyecto', label: 'Proyecto' },
]

const featureCards = [
  {
    title: '🗣 Idioma',
    text: 'El idioma maleku es parte fundamental de la identidad de este pueblo. Actualmente existen esfuerzos para mantener viva la lengua y enseñarla a las nuevas generaciones.',
  },
  {
    title: '🎭 Tradiciones',
    text: 'Los Maleku mantienen relatos tradicionales, artesanías, música y ceremonias que representan su historia y conexión con la naturaleza.',
  },
  {
    title: '🌎 Naturaleza',
    text: 'Los ríos, bosques y animales forman parte importante de la cosmovisión Maleku y de su forma de vida.',
  },
]

const highlight = ref('Tecnología para preservar la cultura Maleku')
</script>

<template>
  <div class="page">
    <header>
      <h1>RedLeds</h1>
      <p>{{ highlight }}</p>
    </header>

    <nav>
      <a v-for="item in navItems" :key="item.href" :href="item.href">{{ item.label }}</a>
    </nav>

    <main>
      <section id="nosotros">
        <div class="card">
          <h2>👋 ¿Quiénes somos?</h2>
          <p>
            ¡Hola! Somos <strong>Matías Sandí Peña</strong> y <strong>Jefrey Rafael Cruz de la O</strong>, integrantes del equipo <strong>RedLeds</strong>.
            Nuestro proyecto busca combinar la robótica y la tecnología para ayudar a preservar y difundir la cultura del pueblo indígena Maleku.
          </p>
        </div>
      </section>

      <section id="maleku">
        <div class="card">
          <h2>🌿 ¿Quiénes son los Maleku?</h2>
          <p>
            Los Maleku son uno de los ocho pueblos indígenas de Costa Rica.
            Habitan principalmente en el cantón de Guatuso, provincia de Alajuela.
            Su cultura conserva un valioso patrimonio de tradiciones, conocimientos e idioma.
          </p>
        </div>
      </section>

      <section class="grid" id="idioma">
        <article v-for="card in featureCards" :key="card.title" class="info">
          <h2>{{ card.title }}</h2>
          <p>{{ card.text }}</p>
        </article>
      </section>

      <section id="proyecto">
        <div class="card">
          <h2>🤖 Nuestro Proyecto</h2>
          <p>
            Con este proyecto queremos demostrar que la tecnología también puede ayudar a proteger el patrimonio cultural.
            Nuestro sistema permite conocer palabras, historia y tradiciones del pueblo Maleku mediante una experiencia interactiva.
          </p>
          <br />
          <h3>Objetivo</h3>
          <p>
            Conservar y difundir la cultura Maleku utilizando herramientas tecnológicas para que más personas conozcan su historia, idioma y tradiciones.
          </p>
        </div>
      </section>
    </main>

    <footer>
      <h3>Equipo RedLeds</h3>
      <p>World Robot Olympiad 2026 • Costa Rica 🇨🇷</p>
    </footer>
  </div>
</template>

<style scoped>
.page {
  min-height: 100vh;
}

header {
  background: linear-gradient(90deg, #b30000, #ff2d2d);
  color: white;
  text-align: center;
  padding: 50px 20px;
}

header h1 {
  font-size: 50px;
}

header p {
  margin-top: 15px;
  font-size: 20px;
}

nav {
  background: #111;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

nav a {
  color: white;
  text-decoration: none;
  padding: 18px;
  transition: 0.3s;
}

nav a:hover {
  background: #c00000;
}

main {
  max-width: 1100px;
  margin: auto;
  padding: 50px 20px;
}

section {
  margin-bottom: 25px;
}

.card {
  background: white;
  border-radius: 15px;
  padding: 25px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #b30000;
  margin-bottom: 15px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.info {
  background: #fafafa;
  padding: 20px;
  border-left: 6px solid #d60000;
  border-radius: 10px;
}

footer {
  background: #111;
  color: white;
  text-align: center;
  padding: 25px;
}
</style>
