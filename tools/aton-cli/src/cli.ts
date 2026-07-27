#!/usr/bin/env node

import { Command } from "commander";
import { doctor } from "./commands/doctor.js";

const program = new Command();

program
  .name("aton")
  .description("ATON Command Line Interface")
  .version("0.1.0");

program
  .command("doctor")
  .description("Check the local development environment")
  .action(doctor);

program.parse();
