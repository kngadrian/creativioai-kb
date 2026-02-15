/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docsSidebar: [
    {type: 'doc', id: 'index', label: 'Home'},
    {type: 'doc', id: 'getting-started', label: 'Getting started'},
    {
      type: 'category',
      label: 'Workflows',
      link: {type: 'doc', id: 'workflows/index'},
      items: ['workflows/index'],
    },
    {
      type: 'category',
      label: 'Features',
      link: {type: 'doc', id: 'features/index'},
      items: [
        'features/create-photoshoot',
        'features/ai-magic-studio',
        'features/ai-magic-tools',
        'features/animation-studio',
        'features/brand-kit',
        'features/agency-dashboard',
      ],
    },
  ],
};

export default sidebars;
