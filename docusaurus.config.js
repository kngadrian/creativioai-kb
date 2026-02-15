// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'CreativioAI Knowledge Base',
  tagline: 'Tutorial-style docs for CreativioAI',
  favicon: 'img/creativio-logo.svg',

  url: 'https://kngadrian.github.io',
  baseUrl: '/creativioai-kb/',

  organizationName: 'kngadrian',
  projectName: 'creativioai-kb',
  trailingSlash: true,

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  stylesheets: [
    {
      href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap',
      type: 'text/css',
    },
  ],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
          editUrl: 'https://github.com/kngadrian/creativioai-kb/edit/main/',
          showLastUpdateAuthor: false,
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/creativio-social.png',
      navbar: {
        title: 'CreativioAI KB',
        logo: {
          alt: 'CreativioAI',
          src: 'img/creativio-logo.svg',
        },
        items: [
          {to: '/', label: 'Docs', position: 'left'},
          {
            href: 'https://github.com/kngadrian/creativioai-kb',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {label: 'Getting Started', to: '/getting-started'},
              {label: 'Workflows', to: '/workflows/'},
              {label: 'Features', to: '/features/'},
            ],
          },
          {
            title: 'Creativio',
            items: [
              {label: 'Website', href: 'https://creativio.io/'},
              {label: 'Special', href: 'https://creativio.io/special'},
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} CreativioAI`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
    }),

};

export default config;
