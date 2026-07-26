import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
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
      items: [],
    },

    {
      type: 'category',
      label: 'Tutorials',
      items: [],
    },

    {
      type: 'category',
      label: 'Community',
      items: [],
    },
  ],
};

export default sidebars;
