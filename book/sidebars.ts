import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      link: {
        type: 'doc',
        id: 'getting-started/index',
      },
      items: [
        'getting-started/intro',
        'getting-started/vision',
        'getting-started/manifesto',
        'getting-started/design-principles',
      ],
    },

    {
      type: 'category',
      label: 'Concepts',
      link: {
        type: 'doc',
        id: 'concepts/index',
      },
      items: [
        'concepts/engineering-operating-system',
        'concepts/artifact',
        'concepts/relation',
        'concepts/version',
      ],
    },

    {
      type: 'category',
      label: 'Reference',
      link: {
        type: 'doc',
        id: 'reference/index',
      },
      items: [
        {
          type: 'category',
          label: 'Architecture',
          items: [
            'reference/architecture/kernel-domain-model',
            'reference/architecture/kernel-service-architecture',
            'reference/architecture/kernel-architecture-rules',
            'reference/architecture/deployment-architecture',
          ],
        },
        {
          type: 'category',
          label: 'Brand',
          items: [
            'reference/brand/brand-guidelines',
          ],
        },
      ],
    },

    {
      type: 'category',
      label: 'Specifications',
      link: {
        type: 'doc',
        id: 'specifications/index',
      },
      items: [],
    },

    {
      type: 'category',
      label: 'Tutorials',
      link: {
        type: 'doc',
        id: 'tutorials/index',
      },
      items: [],
    },

    {
      type: 'category',
      label: 'Community',
      link: {
        type: 'doc',
        id: 'community/index',
      },
      items: [],
    },
  ],
};

export default sidebars;
