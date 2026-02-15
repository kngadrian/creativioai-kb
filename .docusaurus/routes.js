import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/creativioai-kb/',
    component: ComponentCreator('/creativioai-kb/', '9dc'),
    routes: [
      {
        path: '/creativioai-kb/',
        component: ComponentCreator('/creativioai-kb/', '820'),
        routes: [
          {
            path: '/creativioai-kb/',
            component: ComponentCreator('/creativioai-kb/', '56c'),
            routes: [
              {
                path: '/creativioai-kb/features/',
                component: ComponentCreator('/creativioai-kb/features/', 'c2d'),
                exact: true,
                sidebar: "docsSidebar"
              },
              {
                path: '/creativioai-kb/features/agency-dashboard/',
                component: ComponentCreator('/creativioai-kb/features/agency-dashboard/', 'ff0'),
                exact: true,
                sidebar: "docsSidebar"
              },
              {
                path: '/creativioai-kb/features/ai-magic-studio/',
                component: ComponentCreator('/creativioai-kb/features/ai-magic-studio/', '901'),
                exact: true,
                sidebar: "docsSidebar"
              },
              {
                path: '/creativioai-kb/features/ai-magic-tools/',
                component: ComponentCreator('/creativioai-kb/features/ai-magic-tools/', '78f'),
                exact: true,
                sidebar: "docsSidebar"
              },
              {
                path: '/creativioai-kb/features/animation-studio/',
                component: ComponentCreator('/creativioai-kb/features/animation-studio/', '330'),
                exact: true,
                sidebar: "docsSidebar"
              },
              {
                path: '/creativioai-kb/features/brand-kit/',
                component: ComponentCreator('/creativioai-kb/features/brand-kit/', '98c'),
                exact: true,
                sidebar: "docsSidebar"
              },
              {
                path: '/creativioai-kb/features/create-photoshoot/',
                component: ComponentCreator('/creativioai-kb/features/create-photoshoot/', '69d'),
                exact: true,
                sidebar: "docsSidebar"
              },
              {
                path: '/creativioai-kb/getting-started/',
                component: ComponentCreator('/creativioai-kb/getting-started/', '1b4'),
                exact: true,
                sidebar: "docsSidebar"
              },
              {
                path: '/creativioai-kb/workflows/',
                component: ComponentCreator('/creativioai-kb/workflows/', '111'),
                exact: true,
                sidebar: "docsSidebar"
              },
              {
                path: '/creativioai-kb/',
                component: ComponentCreator('/creativioai-kb/', '9fd'),
                exact: true,
                sidebar: "docsSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
