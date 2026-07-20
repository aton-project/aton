import type { ReactNode } from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function Home(): ReactNode {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title={siteConfig.title}
      description="An Open Engineering Operating System"
    >
      <header
        style={{
          padding: '6rem 2rem',
          textAlign: 'center',
        }}
      >
        <Heading as="h1" style={{ fontSize: '4rem' }}>
          ATON
        </Heading>

        <p style={{ fontSize: '1.5rem' }}>
          An Open Engineering Operating System
        </p>

        <p style={{ marginTop: '2rem', fontSize: '1.2rem' }}>
          Engineering Knowledge.
          <br />
          Versioned.
          <br />
          Connected.
          <br />
          Open.
        </p>

        <div style={{ marginTop: '3rem' }}>
          <Link
            className="button button--primary button--lg"
            to="/docs/getting-started/intro"
          >
            Read the Book
          </Link>
        </div>
      </header>
    </Layout>
  );
}
