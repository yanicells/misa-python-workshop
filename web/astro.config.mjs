import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
export default defineConfig({
  site: 'https://yanicells.github.io',
  base: process.env.SITE_BASE || '/misa-python-workshop',
  integrations: [starlight({
    title: 'MISA · Python workshop',
    logo: { src: './public/assets/misa-mark.svg', replacesTitle: false },
    favicon: '/assets/misa-mark.svg',
    social: [{ icon: 'github', label: 'Workshop repository', href: 'https://github.com/yanicells/misa-python-workshop' }],
    customCss: ['./src/styles/custom.css'],
    sidebar: [
      { label: 'Before you begin', items: [{label:'Welcome',slug:''},{label:'Setup and Colab',slug:'setup'}] },
      { label: 'Build your quiz', items: [
        {label:'01 · Make it yours',slug:'build/welcome'},
        {label:'02 · Ask one question',slug:'build/question'},
        {label:'03 · Loop through answers',slug:'build/loops'},
        {label:'04 · Give your code a job',slug:'build/functions'},
        {label:'05 · Show your results',slug:'build/results'},
        {label:'06 · Test and personalize',slug:'build/test'}
      ] },
      { label: 'Keep these handy', items: [{label:'Checkpoints and recovery',slug:'checkpoints'},{label:'Troubleshooting',slug:'help'},{label:'Keep building',slug:'next'},{label:'For facilitators',slug:'facilitators'},{label:'Open Colab notebook',link:'https://colab.research.google.com/github/yanicells/misa-python-workshop/blob/05-results/workshop/misa-quiz.ipynb'}] }
    ]
  })]
});
