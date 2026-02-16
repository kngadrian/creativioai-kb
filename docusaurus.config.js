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
        logo: {
          alt: 'CreativioAI Logo',
          src: 'https://creativio.io/assets/creativio-footer-logo-CYQtbtsV.svg',
          href: 'https://creativio.io',
          width: 160,
        },
        links: [
          {
            title: 'Getting Started',
            items: [
              {label: 'Introduction', to: '/'},
              {label: 'Getting Started Guide', to: '/getting-started'},
              {label: 'Workflows & Examples', to: '/workflows/'},
            ],
          },
          {
            title: 'Features',
            items: [
              {label: 'Create Photoshoot', to: '/features/create-photoshoot'},
              {label: 'AI Magic Tools', to: '/features/ai-magic-tools'},
              {label: 'AI Magic Studio', to: '/features/ai-magic-studio'},
              {label: 'Animation Studio', to: '/features/animation-studio'},
              {label: 'Brand Kit', to: '/features/brand-kit'},
              {label: 'Agency Dashboard', to: '/features/agency-dashboard'},
            ],
          },
          {
            title: 'Resources',
            items: [
              {label: 'CreativioAI Platform', href: 'https://v2.creativio.ai'},
              {label: 'Official Website', href: 'https://creativio.io'},
              {label: 'Pricing', href: 'https://creativio.io/special'},
              {label: 'Video Training', href: 'https://v2.creativio.ai/training'},
            ],
          },
          {
            title: 'Community',
            items: [
              {label: 'GitHub', href: 'https://github.com/kngadrian/creativioai-kb'},
              {label: 'Report an Issue', href: 'https://github.com/kngadrian/creativioai-kb/issues'},
            ],
          },
        ],
        copyright: `
          <div style="margin-top: 24px; padding-top: 24px; border-top: 1px solid rgba(255, 255, 255, 0.1);">
            <p style="margin: 0;">Copyright © ${new Date().getFullYear()} CreativioAI. All rights reserved.</p>
            <p style="margin: 8px 0 0 0; font-size: 0.875rem; opacity: 0.7;">
              Empowering creators with AI-powered visual content tools.
            </p>
          </div>
        `,
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
