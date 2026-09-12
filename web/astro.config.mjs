import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
export default defineConfig({
  integrations: [starlight({
    title: 'Python Workshop',
    logo: { src: './public/assets/misa-mark.svg', replacesTitle: false },
    favicon: '/assets/misa-mark.svg',
    social: [{ icon: 'github', label: 'Workshop repository', href: 'https://github.com/yanicells/misa-python-workshop' }],
    customCss: ['./src/styles/custom.css'],
    components: { Footer: './src/components/Footer.astro' },
    sidebar: [
      { label: 'Before you begin', collapsed: false, items: [
        {label:'Welcome',slug:''},
        {label:'What is Python?',slug:'python'},
        {label:'Git and GitHub',slug:'git-github'},
        {label:'Setup and Colab',slug:'setup'}
      ] },
      { label: 'Build your quiz', collapsed: false, items: [
        {label:'01 · Welcome the player',slug:'build/welcome'},
        {label:'02 · Ask one question',slug:'build/question'},
        {label:'03 · Loop through answers',slug:'build/loops'},
        {label:'04 · Give your code a job',slug:'build/functions'},
        {label:'05 · Show your results',slug:'build/results'},
        {label:'06 · Improve your quiz',slug:'build/improve'},
        {label:'07 · Test and personalize',slug:'build/test'}
      ] },
      { label: 'Moving forward', collapsed: false, items: [
        {label:'Where to go next',slug:'moving-forward'},
        {label:'More with collections',slug:'moving-forward/collections'},
        {label:'Work with text',slug:'moving-forward/text'},
        {label:'Take control of loops',slug:'moving-forward/control-flow'},
        {label:'Transform a list',slug:'moving-forward/list-transformations'},
        {label:'Use Python\'s tools',slug:'moving-forward/tools'},
        {label:'Make functions predictable',slug:'moving-forward/functions'},
        {label:'Build your first class',slug:'moving-forward/objects'},
        {label:'Reuse with inheritance',slug:'moving-forward/inheritance'},
        {label:'Put your work online',slug:'moving-forward/publishing'}
      ] },
      { label: 'Projects', collapsed: false, items: [
        {label:'Pick a project',slug:'projects'},
        {label:'Study planner',slug:'projects/study-planner'},
        {label:'Event budget checker',slug:'projects/event-budget'},
        {label:'Question-bank editor',slug:'projects/question-bank-editor'}
      ] },
      { label: 'Keep these handy', collapsed: false, items: [{label:'Checkpoints and recovery',slug:'checkpoints'},{label:'Troubleshooting',slug:'help'},{label:'For facilitators',slug:'facilitators'},{label:'Open Colab notebook',link:'https://colab.research.google.com/github/yanicells/misa-python-workshop/blob/06-improve/workshop/misa-quiz.ipynb'}] }
    ]
  })]
});
