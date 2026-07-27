export interface ToolStatus {
  name: string;
  installed: boolean;
  version?: string;
}

export interface ProjectStatus {
  gitRepository: boolean;
  foundation: boolean;
  book: boolean;
  tools: boolean;
}

export interface WorkspaceStatus {
  name: string;
  schema: string;
  renderer: string;
}

export interface DoctorReport {
  workspace: WorkspaceStatus;
  project: ProjectStatus;
  tools: ToolStatus[];
}
