
import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'ATON',
tagline: 'An Open Engineering Operating System',
favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://aton-project.org',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'aton-project', // Usually your GitHub org/user name.
  projectName: 'aton', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/social-card.png',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'ATON',
      logo: {
        alt: 'ATON Logo',
        src: 'img/logos/aton-logo.png',
      },
      items: [
        {
          type: 'doc',
          docId: 'getting-started/index',
          label: 'Getting Started',
          position: 'left',
        },
        {
          type: 'doc',
          docId: 'concepts/index',
          label: 'Concepts',
          position: 'left',
        },
        {
          type: 'doc',
          docId: 'reference/architecture/index',
          label: 'Reference',
          position: 'left',
        },
        {
          type: 'doc',
          docId: 'specifications/index',
          label: 'Specifications',
          position: 'left',
        },
        {
          type: 'doc',
          docId: 'tutorials/index',
          label: 'Tutorials',
          position: 'left',
        },
        {
          type: 'doc',
          docId: 'community/index',
          label: 'Community',
          position: 'left',
        },
        {
          href: 'https://github.com/aton-project/aton',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },    
    footer: {
      style: 'dark',
      links: [],
      copyright: `Copyright © ${new Date().getFullYear()} ATON Project.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
