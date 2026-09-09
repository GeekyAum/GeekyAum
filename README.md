<img src="./assets/header.svg" width="100%" alt="Aum Vyas — full-stack engineer, agentic AI systems" />

<div align="center">

<a href="mailto:23ec01005@iitbbs.ac.in"><img src="https://img.shields.io/badge/23ec01005@iitbbs.ac.in-090A0D?style=for-the-badge&logo=maildotru&logoColor=FFB454&labelColor=090A0D" alt="Email"/></a>
<a href="https://linkedin.com/in/aumvyas"><img src="https://img.shields.io/badge/aumvyas-090A0D?style=for-the-badge&logo=linkedin&logoColor=56E0C8&labelColor=090A0D" alt="LinkedIn"/></a>
<a href="https://github.com/GeekyAum"><img src="https://img.shields.io/badge/GeekyAum-090A0D?style=for-the-badge&logo=github&logoColor=D6DAE3&labelColor=090A0D" alt="GitHub"/></a>

</div>

```console
aum@github:~$ whoami

  now      SWE Intern, Google AI Garage — Hyderabad
  school   IIT Bhubaneswar, B.Tech ECE '27 · CGPA 8.98
  build    streaming pipelines, multi-agent orchestration, deterministic gates
  believe  an agent you cannot audit is a liability, not a feature
  below    Verilog, RTL, FSMs — the abstraction leaks and I like knowing where
```

<br/>

<img src="./assets/systems.svg" width="100%" alt="Architecture pattern: sources → ingest → index → route → reason → gate" />

<br/>

## `~/work`

<table>
<tr>
<td width="50%" valign="top">

### 📈 [Meridian](https://github.com/GeekyAum/Meridian)

**Investment research that refuses to guess.** Ingests **5 financial sources** through **4 Kafka + Pathway** pipelines, exposing **15+ market features** over FastAPI on PostgreSQL and MongoDB.

Online **Hoeffding Adaptive Tree** drift detection over **300-tick sliding windows**, with KL/KS divergence tests and 2-confirmation debouncing streaming alerts via Kafka and SSE.

An **Agno + Gemini** decision service exposes **5 read-only MCP tools**, converting drift alerts into evidence-grounded paper-trading workflows behind **4 fail-closed policy gates**. Nothing touches real money — by design.

`260+ host tests` `18 integration tests` `offline-first`

<sub>**Python** · **FastAPI** · **Kafka** · **Pathway** · **PostgreSQL** · **MongoDB** · **Prometheus** · **Docker** · **Agno**</sub>

</td>
<td width="50%" valign="top">

### 🧭 [PathFin](https://github.com/GeekyAum/Dynamic-Agentic-RAG)

**Retrieval that knows how hard the question is.** Embeds **10K+ multi-modal documents** into a **Pathway VectorStore**, sustaining **sub-50 ms** similarity search at **95% LLM-judged precision** across 2K queries.

A **Leader–Analyst multi-agent** system on GPT-4o decomposes and reconciles parallel subtasks, holding orchestration overhead to **200 ms** inside a 35–40 s p95 bounded by LLM inference.

Adaptive RAG context scaling routes queries through a heuristic classifier and planner agent, doubling retrieved documents only on hard queries — **83.9% LLM-judged relevance**.

`0.000 hallucination` under Opik LLM-judge eval

<sub>**Python** · **Pathway VectorStore** · **GPT-4o** · **FastAPI** · **Docker** · **Multi-Agent RAG**</sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🏏 [WittyWicket](https://github.com/GeekyAum/WittyWicket)

**Live sport, narrated by agents.** A real-time commentary pipeline on **Agno** agents and **Pathway VectorStore**, converting streaming match feeds into play-by-play narration grounded in retrieved match history — so the commentary can cite what it's referring to.

Sport-specific ingestion sits behind a common **adapter interface**: **4 scrapers** ship today for cricket, football, basketball and tennis, and a new sport plugs in by implementing one interface.

<sub>**Python** · **Agno** · **Pathway** · **Docker** · **Web scraping**</sub>

</td>
<td width="50%" valign="top">

### 🗄️ Elsewhere

**[Digital-Design](https://github.com/GeekyAum/Digital-Design)** — Verilog HDL reference designs. RTL, finite state machines, FPGA fundamentals.

**[narrative-core](https://github.com/GeekyAum/narrative-core)** — AI-driven storytelling system; contributing upstream.

**[Portfolio](https://github.com/GeekyAum/Portfolio)** — hand-built personal site. HTML, CSS, vanilla JS, no framework, no build step.

<br/>

> 🏆 **Inter IIT Tech Meet 13.0** — 8th of 23 IITs, Pathway problem statement
> 🥇 **GC 2025 ML Hackathon**, IIT Bhubaneswar — 1st place

</td>
</tr>
</table>

<br/>

## `~/experience`

<details open>
<summary><b>Google · AI Garage</b> &nbsp;—&nbsp; <i>Software Engineering Intern</i> &nbsp;·&nbsp; Hyderabad &nbsp;·&nbsp; May – Aug 2026</summary>

<br/>

- Architected a **Python SDK for multi-party calendar negotiation** on a **hexagonal (ports-and-adapters)** architecture — event-command design with **6 swappable adapters**, across **60+ peer-reviewed changelists**.
- Built the negotiation core on **dual finite-state machines** with multi-round consensus, eliminating double-booking race conditions via **Try-Confirm-Cancel** reservations and auto-expiring pessimistic locks.
- Shipped the SDK into an internal scheduling app through a **3-node Google ADK workflow** wiring **Google Calendar REST APIs**, **OAuth 2.0**, Pydantic validation, **Gemini** reasoning and **Cloud Spanner** persistence.
- Hardened reliability with unit and **polymorphic contract tests**; profiled **P90 latency**, token throughput and **cProfile** to hold **sub-100 ms** SDK overhead and isolate LLM inference as the dominant bottleneck.

</details>

<br/>

## `~/stack`

<table>
<tr>
<td valign="top" width="34%">

**AI &amp; agents**

<img src="https://img.shields.io/badge/PyTorch-090A0D?style=flat-square&logo=pytorch&logoColor=FFB454" alt="PyTorch"/>
<img src="https://img.shields.io/badge/Hugging%20Face-090A0D?style=flat-square&logo=huggingface&logoColor=FFB454" alt="Hugging Face"/>
<img src="https://img.shields.io/badge/LangChain-090A0D?style=flat-square&logo=langchain&logoColor=56E0C8" alt="LangChain"/>
<img src="https://img.shields.io/badge/LangGraph-090A0D?style=flat-square&logo=langgraph&logoColor=56E0C8" alt="LangGraph"/>
<img src="https://img.shields.io/badge/Gemini-090A0D?style=flat-square&logo=googlegemini&logoColor=56E0C8" alt="Gemini"/>
<img src="https://img.shields.io/badge/Agno-090A0D?style=flat-square&logoColor=D6DAE3" alt="Agno"/>
<img src="https://img.shields.io/badge/Multi--Agent%20RAG-090A0D?style=flat-square&logoColor=D6DAE3" alt="Multi-Agent RAG"/>

</td>
<td valign="top" width="33%">

**Backend &amp; data**

<img src="https://img.shields.io/badge/Python-090A0D?style=flat-square&logo=python&logoColor=FFB454" alt="Python"/>
<img src="https://img.shields.io/badge/C++-090A0D?style=flat-square&logo=cplusplus&logoColor=56E0C8" alt="C++"/>
<img src="https://img.shields.io/badge/FastAPI-090A0D?style=flat-square&logo=fastapi&logoColor=56E0C8" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Kafka-090A0D?style=flat-square&logo=apachekafka&logoColor=D6DAE3" alt="Kafka"/>
<img src="https://img.shields.io/badge/PostgreSQL-090A0D?style=flat-square&logo=postgresql&logoColor=56E0C8" alt="PostgreSQL"/>
<img src="https://img.shields.io/badge/MongoDB-090A0D?style=flat-square&logo=mongodb&logoColor=56E0C8" alt="MongoDB"/>
<img src="https://img.shields.io/badge/Pathway-090A0D?style=flat-square&logoColor=D6DAE3" alt="Pathway"/>
<img src="https://img.shields.io/badge/OAuth%202.0-090A0D?style=flat-square&logo=auth0&logoColor=FFB454" alt="OAuth 2.0"/>

</td>
<td valign="top" width="33%">

**Ops &amp; silicon**

<img src="https://img.shields.io/badge/Docker-090A0D?style=flat-square&logo=docker&logoColor=56E0C8" alt="Docker"/>
<img src="https://img.shields.io/badge/Prometheus-090A0D?style=flat-square&logo=prometheus&logoColor=FFB454" alt="Prometheus"/>
<img src="https://img.shields.io/badge/Grafana-090A0D?style=flat-square&logo=grafana&logoColor=FFB454" alt="Grafana"/>
<img src="https://img.shields.io/badge/Google%20ADK-090A0D?style=flat-square&logo=googlecloud&logoColor=56E0C8" alt="Google ADK"/>
<img src="https://img.shields.io/badge/Git-090A0D?style=flat-square&logo=git&logoColor=FFB454" alt="Git"/>
<img src="https://img.shields.io/badge/TypeScript-090A0D?style=flat-square&logo=typescript&logoColor=56E0C8" alt="TypeScript"/>
<img src="https://img.shields.io/badge/Verilog-090A0D?style=flat-square&logoColor=A07CFF" alt="Verilog"/>

</td>
</tr>
</table>

<br/>

## `~/signal`

<div align="center">

<img height="160" src="https://github-readme-stats.vercel.app/api?username=GeekyAum&show_icons=true&hide_border=true&include_all_commits=true&bg_color=090A0D&title_color=FFB454&text_color=D6DAE3&icon_color=56E0C8&ring_color=FFB454" alt="GitHub stats"/>
<img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=GeekyAum&layout=compact&langs_count=8&hide_border=true&bg_color=090A0D&title_color=FFB454&text_color=D6DAE3" alt="Top languages"/>

</div>

<br/>

## `~/contact`

Open to **internships and full-time roles** in AI engineering and backend systems.
If you're building something that has to think — and has to be right — I'd like to hear about it.

<div align="center">
<br/>

<a href="mailto:23ec01005@iitbbs.ac.in"><img src="https://img.shields.io/badge/Email-FFB454?style=for-the-badge&logo=maildotru&logoColor=090A0D&labelColor=FFB454" alt="Email"/></a>
<a href="https://linkedin.com/in/aumvyas"><img src="https://img.shields.io/badge/LinkedIn-090A0D?style=for-the-badge&logo=linkedin&logoColor=56E0C8&labelColor=090A0D" alt="LinkedIn"/></a>
<a href="https://github.com/GeekyAum"><img src="https://img.shields.io/badge/GitHub-090A0D?style=for-the-badge&logo=github&logoColor=D6DAE3&labelColor=090A0D" alt="GitHub"/></a>

<br/><br/>

<sub><code>Student Internship Coordinator · Career Development Cell, IIT Bhubaneswar</code></sub><br/>
<sub><code>Governor · Society of Finance, Economics, Business and Data Science</code></sub>

</div>
