import { Container, getContainer } from "@cloudflare/containers";

interface Env {
  AGENT: DurableObjectNamespace<LanggraphAgent>;
  OPENAI_API_KEY: string;
  OPENAI_BASE_URL: string;
  SIMPLE_AGENT_MODEL: string;
  ANTHROPIC_API_KEY?: string;
}

export class LanggraphAgent extends Container<Env> {
  defaultPort = 2024;
  sleepAfter = "10m" as const;

  constructor(...args: ConstructorParameters<typeof Container<Env>>) {
    super(...args);
    const env = args[1];
    this.envVars = {
      OPENAI_API_KEY: env.OPENAI_API_KEY,
      OPENAI_BASE_URL: env.OPENAI_BASE_URL,
      SIMPLE_AGENT_MODEL: env.SIMPLE_AGENT_MODEL,
      ANTHROPIC_API_KEY: env.ANTHROPIC_API_KEY ?? "",
    };
  }
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    return getContainer(env.AGENT, "singleton").fetch(request);
  },
};
