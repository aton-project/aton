import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  bookSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      collapsed: false,
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
      collapsed: false,
      items: [
        'concepts/engineering-operating-system',
        'concepts/artifact',
        'concepts/relation',
        'concepts/version',
      ],
    },

    {
      type: 'category',
      label: 'Architecture',
      collapsed: false,
      items: [
        'architecture/kernel-domain-model',
        'architecture/kernel-service-architecture',
        'architecture/kernel-architecture-rules',
      ],
    },

    {
      type: 'category',
      label: 'Decisions',
      collapsed: false,
      items: [
        'decisions/aton-vision',
        'decisions/engineering-knowledge-graph',
        'decisions/everything-is-an-artifact',
        'decisions/git-source-of-truth',
        'decisions/emf-implementation-model',
      ],
    },
  ],
};

export default sidebars;
