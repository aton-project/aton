export interface ManifestData {

  schema: string;

  workspace: {
    name: string;
  };

  foundation: {
    path: string;
  };

  renderer: {
    default: string;
  };

  book: {
    path: string;
  };

  cli: {
    minimumVersion: string;
  };

}
