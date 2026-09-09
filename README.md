```
 █████╗ ██╗   ██╗███╗   ███╗    ██╗   ██╗██╗   ██╗ █████╗ ███████╗
██╔══██╗██║   ██║████╗ ████║    ██║   ██║╚██╗ ██╔╝██╔══██╗██╔════╝
███████║██║   ██║██╔████╔██║    ██║   ██║ ╚████╔╝ ███████║███████╗
██╔══██║██║   ██║██║╚██╔╝██║    ╚██╗ ██╔╝  ╚██╔╝  ██╔══██║╚════██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║     ╚████╔╝    ██║   ██║  ██║███████║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝      ╚═══╝     ╚═╝   ╚═╝  ╚═╝╚══════╝
      i build agents that are not allowed to make things up
```

```
   \\ //
   (o.o)    "oh — hi. didn't think anyone actually scrolled up here."
  <(   )>~
    ^ ^     "i'm chip. i live in this repo. i'll show you around."
```

|  |  |
|---|---|
| `[1]` [who even is this](#whoami) | `[4]` [what he can actually do](#stack) |
| `[2]` [the three real ones](#work) | `[5]` [receipts](#proof) |
| `[3]` [the google thing](#google) | `[6]` [how to reach him](#contact) |

<br>

<a id="whoami"></a>
## `[1]` who even is this

```console
$ whoami

  aum vyas  ·  @GeekyAum
  b.tech electronics & communication '27  ·  iit bhubaneswar  ·  cgpa 8.98
  swe intern @ google ai garage  ·  hyderabad  ·  may–aug 2026

$ cat ~/.thesis

  everyone can get a model to say something.
  the hard part is making it prove it, and stopping it when it can't.
  so i build the boring half: streaming ingest, live indexes,
  routers, and gates that fail closed.
```

```
   \\ //
   (o.o)    "he means it. every project down there has a part
  <(   )>    whose entire job is telling the ai to shut up."
    ^ ^
```

<br>

<a id="work"></a>
## `[2]` the three real ones

Everything he builds ends up the same shape. Chip drew it:

```
  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
  │  1 INGEST   │──▶│  2 INDEX    │──▶│  3 ROUTE    │──▶│  4 REASON   │──▶│  5 GATE     │
  ├─────────────┤   ├─────────────┤   ├─────────────┤   ├─────────────┤   ├─────────────┤
  │ kafka       │   │ pathway     │   │ heuristic   │   │ leader ·    │   │ evidence    │
  │ 4 pipelines │   │ vectorstore │   │ classifier  │   │ analyst     │   │ grounding   │
  │ 5 feeds     │   │ 10k+ docs   │   │ drift tree  │   │ agents      │   │ 4 hard nos  │
  └─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
                       sub-50 ms                        200 ms overhead    fails closed
  └───────────────── deterministic ─────────────────┘   └── the llm ──┘   └─── gated ───┘

  the model gets exactly one stage. everything on either side of it is code
  that can be tested, and that is the entire trick.
```

### 📈 [Meridian](https://github.com/GeekyAum/Meridian) · *investment research that won't spend your money*

> ```
>  \\ //
>  (o.o)   "it can recommend. it cannot buy. there is a
> <(   )>   wall between those two verbs and i helped build it."
>   ^ ^
> ```

- Ingests **5 financial sources** through **4 Kafka + Pathway** pipelines, exposing **15+ market features** over FastAPI on PostgreSQL and MongoDB.
- Online **Hoeffding Adaptive Tree** drift detection over **300-tick sliding windows** — KL/KS divergence tests, 2-confirmation debouncing, alerts out over Kafka and SSE.
- An **Agno + Gemini** decision service exposes **5 read-only MCP tools**, turning drift alerts into evidence-grounded paper trades behind **4 fail-closed policy gates**.
- `260+ host tests` · `18 integration tests` · offline-first, no live broker, no real money.

<sub>`python` `fastapi` `kafka` `pathway` `postgresql` `mongodb` `prometheus` `grafana` `docker` `agno`</sub>

### 🧭 [PathFin](https://github.com/GeekyAum/Dynamic-Agentic-RAG) · *retrieval that sizes you up first*

> ```
>  \\ //
>  (o.o)   "it decides how hard your question is before
> <(   )>   it answers. a little rude. extremely effective."
>   ^ ^
> ```

- **10K+ multi-modal documents** embedded into a **Pathway VectorStore**, holding **sub-50 ms** similarity search at **95% LLM-judged precision** over 2K queries.
- A **Leader–Analyst multi-agent** system on GPT-4o decomposes and reconciles parallel subtasks — **200 ms** orchestration overhead inside a 35–40 s p95 that's all LLM inference.
- Adaptive context scaling routes through a heuristic classifier and planner agent, doubling retrieved documents *only* on hard queries — **83.9% LLM-judged relevance**, `0.000` hallucination.

<sub>`python` `pathway vectorstore` `gpt-4o` `fastapi` `docker` `multi-agent rag` `opik`</sub>

### 🏏 [WittyWicket](https://github.com/GeekyAum/WittyWicket) · *live sport, narrated by agents*

> ```
>  \\ //
>  (^o^)   "this one's my favourite and i refuse to
> <(   )>   explain why. no follow-up questions."
>   ^ ^
> ```

- Real-time commentary pipeline on **Agno** agents and **Pathway VectorStore**, turning streaming match feeds into play-by-play narration grounded in retrieved match history — it can cite the over it's talking about.
- Sport-specific ingestion hides behind one **adapter interface**: **4 scrapers** ship today (cricket, football, basketball, tennis) and a new sport is one interface away.

<sub>`python` `agno` `pathway` `docker` `web scraping`</sub>

<details>
<summary><b>🗄️ the shelf out back</b> — smaller things, forks, and one Verilog rabbit hole</summary>

<br>

- **[Digital-Design](https://github.com/GeekyAum/Digital-Design)** — Verilog HDL reference designs. RTL, finite state machines, FPGA fundamentals. The ECE degree occasionally demands tribute.
- **[narrative-core](https://github.com/GeekyAum/narrative-core)** — AI-driven storytelling system, contributing upstream.
- **[Portfolio](https://github.com/GeekyAum/Portfolio)** — hand-built personal site. HTML, CSS, vanilla JS. No framework, no build step, no regrets.

</details>

<br>

<a id="google"></a>
## `[3]` the google thing

```console
$ cat ~/experience/google-ai-garage.md

  Software Engineering Intern · AI Garage · Hyderabad · May – Aug 2026
```

- Architected a **Python SDK for multi-party calendar negotiation** on a **hexagonal (ports-and-adapters)** architecture — event-command design, **6 swappable adapters**, **60+ peer-reviewed changelists**.
- Built the negotiation core on **dual finite-state machines** with multi-round consensus, killing double-booking race conditions via **Try-Confirm-Cancel** reservations and auto-expiring pessimistic locks.
- Shipped it into an internal scheduling app through a **3-node Google ADK workflow** wiring **Google Calendar REST APIs**, **OAuth 2.0**, Pydantic validation, **Gemini** reasoning and **Cloud Spanner** persistence.
- Hardened it with unit and **polymorphic contract tests**; profiled **P90 latency**, token throughput and **cProfile** to hold **sub-100 ms** SDK overhead — and to prove the LLM was the bottleneck, not the code.

```
   \\ //
   (o_O)   "two state machines, in a calendar app, so that
  <(   )>   nobody double-books a meeting room. i think about
    ^ ^     this more than a cricket reasonably should."
```

<br>

<a id="stack"></a>
## `[4]` what he can actually do

```
~/stack
│
├── ai/
│   ├── agents      agno · langgraph · langchain · multi-agent orchestration
│   ├── models      gemini · gpt-4o · pytorch · hugging face
│   └── retrieval   pathway vectorstore · adaptive rag · opik llm-judge eval
│
├── backend/
│   ├── languages   python · c++ · sql          (familiar: c, js, ts, protobuf)
│   ├── serving     fastapi · rest · oauth 2.0 · google adk
│   └── data        kafka · postgresql · mongodb · cloud spanner
│
├── ops/
│   └── docker · git · prometheus · grafana
│
├── cs/
│   └── dsa · oop · operating systems · database systems
│
└── silicon/
    └── verilog · rtl · fsm design       # not a job requirement. still fun.
```

<br>

<a id="proof"></a>
## `[5]` receipts

```diff
+ Inter IIT Tech Meet 13.0        8th of 23 IITs — Pathway problem statement    Dec 2024
+ General Championship 2025       1st place, ML Hackathon, IIT Bhubaneswar      Mar 2025
! Student Internship Coordinator  Career Development Cell, IIT BBS         Apr '25 – Mar '26
! Governor                        Society of Finance, Economics, Business
                                  and Data Science, IIT BBS                Apr '25 – Mar '26
```

<br>

<a id="contact"></a>
## `[6]` how to reach him

```
   \\ //
   (o.o)   "he answers email. he is a student. of course he answers email."
  <(   )>
    ^ ^
```

**Open to internships and full-time roles** in AI engineering and backend systems.
If you're building something that has to think *and* has to be right — that's the interesting part.

| | |
|---|---|
| 📮 **email** | [23ec01005@iitbbs.ac.in](mailto:23ec01005@iitbbs.ac.in) |
| 💼 **linkedin** | [in/aumvyas](https://linkedin.com/in/aumvyas) |
| 🐙 **github** | [@GeekyAum](https://github.com/GeekyAum) |

<br>

---

<details>
<summary><b>🦗 poke chip</b></summary>

<br>

```
   \\ //
   (>_<)   "OW."
  <(   )>
    ^ ^

   \\ //
   (-_-)   "...fine. a fact, and then you leave me alone:
  <(   )>   'crickets' is what you hear when a repo has no commits.
    ^ ^     i am, structurally, a threat. behave."
```

</details>

<details>
<summary><b>🤔 why a cricket, though</b></summary>

<br>

Three reasons, and they're all the same reason:

1. **WittyWicket** does live *cricket* commentary.
2. He's an **ECE** student — so the pet is named **Chip**.
3. 🦗 is the universal sound of a dead repository. Keeping one alive on the profile felt like the right kind of threat.

```
   \\ //
   (^_^)   "the third one is the real one."
  <(   )>
    ^ ^
```

</details>

<details>
<summary><b>📄 recruiter mode</b> — the same page, with the cricket removed</summary>

<br>

**Aum Vyas** — B.Tech Electronics & Communication Engineering, IIT Bhubaneswar (2023–2027), CGPA 8.98/10.

**Experience** — Software Engineering Intern, Google AI Garage, Hyderabad (May–Aug 2026). Architected a Python SDK for multi-party calendar negotiation using hexagonal architecture with 6 swappable adapters across 60+ peer-reviewed changelists; built a dual-FSM negotiation core with Try-Confirm-Cancel reservations; shipped via a 3-node Google ADK workflow over Google Calendar APIs, OAuth 2.0, Gemini and Cloud Spanner; held sub-100 ms SDK overhead under P90 latency profiling.

**Projects** — *Meridian*: real-time investment research platform, 5 data sources, 4 Kafka/Pathway pipelines, Hoeffding-tree drift detection, agentic decision layer behind 4 fail-closed gates, 260+ tests. *PathFin*: agentic RAG over 10K+ documents, sub-50 ms retrieval at 95% precision, Leader–Analyst multi-agent orchestration at 200 ms overhead, 83.9% LLM-judged relevance. *WittyWicket*: real-time AI sports commentary on Agno and Pathway, adapter-based ingestion across 4 sports.

**Skills** — Python, C++, SQL (adept); C, JavaScript, TypeScript, HTML/CSS, Protocol Buffers (familiar). FastAPI, REST, OAuth 2.0, Kafka, Cloud Spanner, PostgreSQL, MongoDB. Docker, Git, Google ADK, Prometheus, Grafana, Pathway. PyTorch, Hugging Face, LangChain, LangGraph, Agno, RAG, multi-agent systems. Verilog, RTL, FSM design.

**Achievements** — Inter IIT Tech Meet 13.0: 8th of 23 IITs (Pathway). GC 2025 ML Hackathon, IIT Bhubaneswar: 1st place.

**Contact** — [23ec01005@iitbbs.ac.in](mailto:23ec01005@iitbbs.ac.in) · [linkedin.com/in/aumvyas](https://linkedin.com/in/aumvyas)

</details>

<br>

```
                                    \\ //
   chip's hunger    ▓▓▓▓▓▓▓░░░      (-.-)  zZ
   feed him by starring a repo     <(   )>
                                     ^ ^
```
