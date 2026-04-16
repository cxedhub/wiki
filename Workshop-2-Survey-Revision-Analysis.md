# Workshop 2 Survey Revision — Analysis and Modification Options

**Prepared:** 2026-04-16
**Context:** CRAFT PD Series (NSF WRNN, UCF IRB STUDY00007380). W1 surveys are finalized (workshop complete). W2 Pre/Post are revisable ahead of the April 18 session. Purpose of this document is to propose modification strategies aligned with the manuscript draft (Borowczak & Borowczak, *Ed Sci* MDPI SI, submission deadline 2026-04-30).

---

## 1. Diagnostic summary

The manuscript's central empirical claim is the **C2 effect-size asymmetry**: the Fortify-aligned item (confidence identifying errors in AI-generated content) produced d\_rm = +0.77 after W1, versus +1.42 to +2.12 for the other four Likert items. The manuscript argues this asymmetry is theoretically expected and proposes a multi-session follow-up as Future Work item (i): *"a multi-session study testing whether the C2 effect-size gap closes with repeated Fortify practice."*

**As currently written, W2 cannot answer this question.** W2 Pre/Post do not re-administer W1's C1 or C2 items. W2C2 ("confidence addressing academic integrity concerns") is a different construct than W1C2 ("confidence identifying errors"). For the subset of repeat attendees, there is no longitudinal measurement of the exact disposition the paper hinges on.

This is the highest-leverage change. All other revisions are secondary.

## 2. CRAFT-phase mapping of existing instruments

### W1 (fixed)
| CRAFT phase | Item | Construct |
|---|---|---|
| Contextualize | — | (delivered via 3-LLM side-by-side; not surveyed) |
| Reframe | K1 | LLM understanding |
| Reframe | K3 | Platform differences |
| Assemble | K2 | Prompt-writing ability |
| Assemble | C1 | Confidence using AI for STEM teaching |
| **Fortify** | **C2** | **Confidence identifying errors** — only Fortify item |
| Transfer | P1 (pre) | Current frequency of AI use |
| Transfer | P2 (post) | Likelihood of use within next month |
| Transfer | R1, R2 (post) | Open-response adoption commitments |

### W2 (current, revisable)
| CRAFT phase | Item | Construct | Note |
|---|---|---|---|
| Contextualize | — | — | Gap |
| Reframe | K1 | Understanding of AI error modes | W2-specific; keep |
| Assemble | — | — | Gap |
| Fortify | K2 | Systematically verify AI-generated code | Code-specific; keep |
| Fortify | K3 | Familiarity with CtM / verification frameworks | Keep |
| Fortify | C1 | Confidence teaching students to evaluate AI | Pedagogical enactment; keep |
| Adjacent (not Fortify) | C2 | Confidence addressing academic-integrity concerns | Reclassify |
| Transfer | R1, R2 (post) | Open-response reflection on W2 content | Keep |

### W3 (for context, not revised here)
W3 measures Edge/IoT-specific constructs and has no CRAFT-anchor items carried forward. Option C below recommends adding the cross-workshop anchor items to W3 as well.

### Key observations

1. **W2 is the "Fortify workshop" topically but under-measures Fortify** relative to W1. W1 had one broad Fortify item; W2 has three topic-specific ones but no item that parallels W1's general disposition measure.
2. **W2 has no behavioral-intent item at post.** W1 had P2 ("how likely to use AI within next month"). A W2-specific Fortify intent item would fill this.
3. **W2 has no Assemble-phase measure.** Given W2's structure includes hands-on verification exercises, an Assemble-adjacent item (e.g., confidence designing a verification protocol) would be appropriate.
4. **W2 Pre does not ask whether participants attended W1.** For the repeat-participant subgroup, this is a critical branching question. Without it, longitudinal analyses rely entirely on PARTICIPANT_ID matching (which, per the manuscript's §4.4.1, was already non-trivial at N=16).
5. **Scale anchor drift.** Minor but worth correcting:
   - W1K1 "1 - No understanding … 5 - Strong understanding" → W2K1 drops "understanding" at the endpoint.
   - W1K2 "1 - Cannot do this" → W2K2 "1 - Cannot".
   - For cross-survey pooling these should be identical.

## 3. Three modification options

### Option A — Minimal continuity

**Goal:** Make the manuscript's follow-up hypothesis testable. Nothing more.

**Change list:**
1. Add a new block to W2 Pre and W2 Post titled *"CRAFT Cross-Workshop Anchor (repeat items)"* containing:
   - `W1C1` verbatim: "How confident are you in using AI tools to support your STEM teaching?" (1 = Not confident … 5 = Very confident)
   - `W1C2` verbatim: "How confident are you in identifying errors in AI-generated STEM content?" (1 = Not confident … 5 = Very confident)
   - `W1P2` verbatim (Post only): "How likely are you to use AI tools for lesson planning within the next month?" (1 = Very unlikely … 5 = Very likely)
2. Add one branching item at the top of W2 Pre's *About You* block:
   - "Did you attend Workshop 1 on April 11?" [Yes / No / Partially]
3. Fix scale-anchor drift on W2K1 and W2K2 to match W1 wording.

**Burden:** ~3 extra Likert items on Pre (~30 sec), ~4 on Post (~40 sec). Total added time well under a minute.

**What this enables:**
- Within-W2 pre/post on the canonical C1 and C2 items.
- W1→W2 longitudinal on C1 and C2 for repeat participants (matched by PARTICIPANT_ID).
- Direct test of the manuscript's Future Work hypothesis on the smaller multi-session subsample.

**What this does *not* enable:**
- Resolution into Fortify sub-techniques. The single C2 item remains broad.
- CRAFT-framework awareness as a distinct construct.
- Classroom-enactment evidence between W1 and W2.

---

### Option B — Moderate revision (recommended)

**Goal:** Option A plus (i) higher-resolution Fortify measurement, (ii) explicit CRAFT awareness, (iii) distal outcome capture between sessions.

**Change list (in addition to Option A):**

**B1. Split C2 into three Fortify sub-technique items.** Keep the unitary W1C2 verbatim as an anchor, but add three new items measuring the specific techniques modeled in the workshops. All three should appear on both Pre and Post, both workshops going forward.

Proposed wording (1 = Not confident / 5 = Very confident):
- `FORT1`: "How confident are you in comparing outputs from two or more LLMs on the same prompt to verify accuracy?"
- `FORT2`: "How confident are you in cross-checking AI-generated claims against authoritative sources (textbooks, peer-reviewed articles, official curricula)?"
- `FORT3`: "How confident are you in designing adversarial prompts to probe whether an AI output is reliable?"

Rationale: the manuscript describes Fortify activities in §3.1 and §4.2 as cross-LLM comparison, authoritative-source verification, and adversarial probing. The three sub-items operationalize that definition and give you resolution to detect effects the single broad C2 item may be averaging over.

**B2. Add a CRAFT-framework awareness item.** The manuscript reports (§5.3 Theme 3) that "CRAFT was named without prompting in 5 [of 19] adoption-intent responses (26%)." This is currently only captured qualitatively. Add to both Pre and Post:

- `CRAFT_KNOW`: "How familiar are you with the CRAFT pedagogical cycle?" (1 = Never heard of it / 2 = Heard of it / 3 = Can name some phases / 4 = Can use in lesson planning / 5 = Have taught with it)

**B3. Add W1-enactment block to W2 Pre** (branches on "Did you attend W1?" = Yes/Partially):

- `W1E1`: "Since Workshop 1, have you used any AI tool for a teaching-related task?" [No / Once or twice / A few times / Regularly]
- `W1E2`: "Since Workshop 1, have you done any of the following? (Select all that apply)"
   - Compared outputs across two or more LLMs
   - Checked an AI output against an authoritative source
   - Used the CRAFT lesson-prompt template
   - Shared what you learned with a colleague
   - Modified a lesson based on AI output
   - None of the above
- `W1E3` (open, optional): "Briefly describe one thing you tried between W1 and W2."

Rationale: directly addresses the Limitations paragraph in §5.6 ("we do not yet measure whether teachers' subsequent students behave differently, or whether the adoption plans articulated in Theme 3 were enacted"). Retrospective self-report is imperfect but it's what's feasible here.

**B4. Add a W2-specific Fortify intent item to W2 Post:**

- `W2P1`: "How likely are you to systematically verify AI outputs (e.g., using cross-LLM comparison or the Check the Machine protocol) before using them in your classroom within the next month?" (1 = Very unlikely / 5 = Very likely)

**Burden:** Approximately 8 extra items on Pre (~2 min), 7 extra on Post (~1.5 min). Total pre: ~4-5 minutes instead of ~3. Total post: ~5-6 minutes instead of ~4.

**What this enables (beyond Option A):**
- Testing whether Fortify effect-size asymmetry is driven by a specific technique vs. all three (a sharper version of the manuscript's claim).
- Measuring CRAFT vocabulary uptake explicitly rather than only through unprompted mentions.
- A preliminary distal outcome (self-reported enactment) for W1 participants — a partial response to §5.6 Limitations.
- Workshop-specific intent for W2 that parallels W1P2.

**IRB implication:** This is a more substantial modification than Option A and likely requires a formal amendment to STUDY00007380. Estimated timeline per UCF HRP-254 norms is 2–4 weeks; this would need to be submitted immediately if W2 is on April 18.

---

### Option C — Comprehensive longitudinal instrument

**Goal:** Transform the CRAFT PD series into a three-timepoint longitudinal study explicitly designed to support the manuscript's follow-up work and a second publication on cross-session growth trajectories.

**Change list (in addition to Options A and B):**

**C1. Add CRAFT-phase knowledge matching.** Short 5-item block on Post (both W2 and W3), testing recognition of each phase's role:
- Matching format: "Which CRAFT phase primarily involves [establishing a motivating anchor / formalizing into disciplinary vocabulary / constructing the artifact / gathering evidence against the artifact / applying to a new context]?"

This gives a knowledge-level measure of the framework rather than only familiarity or enactment.

**C2. Behavioral-frequency items (not just self-efficacy).** Desimone (2009), cited in the manuscript, distinguishes proximal from distal outcomes. Self-efficacy is proximal; frequency of the target behavior is closer to distal. Add to W2 Pre and W3 Pre:

- "In the past two weeks, how many times have you (a) used an LLM for a teaching task, (b) compared outputs across LLMs, (c) verified an AI output against an authoritative source?" [0 / 1 / 2 / 3+ for each]

**C3. Propagate the cross-workshop anchor to W3.** Add W1C1, W1C2, and the three FORT items to W3 Pre and Post. This gives three measurement points on the same constructs across the April 11 → April 18 → April 25 series.

**C4. Add a final cross-workshop post-series survey** (4–6 weeks after W3) that re-administers the anchor items one more time, plus retrospective items on enacted classroom changes. This is the most consequential addition: it would move the study from "single-session PD with a follow-up hypothesis" to "multi-session PD with an actual durability measure," materially strengthening any follow-on manuscript.

**Burden:** Adds another ~3 minutes across the three workshops. Adds a new delayed post-series instrument that participants have not consented to yet.

**IRB implication:** Full amendment required. The delayed post-series survey is a material addition that changes the time-burden disclosure in the consent language. This is not doable in time for the April 18 W2 session but could be staged: do Option B for W2, submit Option C amendment for W3.

---

## 4. Recommendation

For the April 18 W2 session, **Option B is the recommended path**. Rationale:

1. It makes the manuscript's Future Work item (i) testable with the Pre/Post delta and the subset of repeat attendees — directly buying measurement support for the paper's central follow-up claim.
2. It addresses the highest-impact item in the Limitations section (self-report of classroom enactment) through the B3 retrospective block, without requiring a new instrument or a new consent pathway.
3. It resolves the single broad C2 into three specific Fortify techniques, which lets you test whether the smaller C2 effect is driven by one technique (e.g., adversarial prompting, which is the least intuitive) or by all three uniformly. That distinction is publishable on its own.
4. It keeps W3 untouched for now, preserving the option to pursue Option C as a planned extension rather than a rushed retrofit.

Option A is the fallback if an IRB amendment cannot be processed before April 18. Option A's changes are substantively small enough to potentially qualify as an administrative modification rather than a full amendment — **this should be confirmed with the UCF IRB coordinator before assuming**.

Option C is the long game: propose it as a planned extension in the manuscript's §5.7 Future Work, and initiate the amendment to support it in parallel with submission.

## 5. IRB and operational considerations

| Concern | Option A | Option B | Option C |
|---|---|---|---|
| Likely amendment type | Administrative / minor | Formal amendment | Formal amendment + new instrument |
| Estimated IRB turnaround | 1–5 business days | 2–4 weeks | 4–6 weeks |
| Added participant burden | < 1 min | ~3 min Pre, ~2 min Post | ~5 min total + new delayed survey |
| Consent re-signing? | No | No (amendment to existing consent) | Likely yes, for delayed post-series |
| Feasibility before 2026-04-18 W2 | High | Tight — submit today | No |

## 6. Specific edits to implement Option B

If Option B is approved, the concrete W2 survey edits are below. **Implementation note:** Qualtrics Advanced Format (the text-file import you're using) does not support inline display-logic syntax. The `[[DisplayLogic: ...]]` markers in the snippets below are annotations — after importing the text file, the three W1-enactment items (W1E1, W1E2, W1E3) need to have display logic set in the Qualtrics editor so they show only when `W1_ATTEND` ≠ "No". Alternatively, keep them unconditional on the Pre and let non-attendees answer "No" / "None of the above" — slightly cleaner data but longer survey for first-time participants.


### W2 Pre-Survey

Insert after current *About You* block (i.e., after EXPERIENCE item), new block *W1 Attendance and Enactment*:

```
[[Block:W1 Attendance and Enactment]]

[[Question:MC:SingleAnswer]]
[[ID:W1_ATTEND]]
Did you attend Workshop 1 (Using AI for STEM, April 11)?
[[Choices]]
Yes, fully
Yes, partially
No

[[PageBreak]]

[[Question:MC:SingleAnswer]]
[[ID:W1E1]]
[[DisplayLogic: W1_ATTEND != "No"]]
Since Workshop 1, have you used any AI tool for a teaching-related task?
[[Choices]]
No
Once or twice
A few times
Regularly

[[Question:MC:MultipleAnswer]]
[[ID:W1E2]]
[[DisplayLogic: W1_ATTEND != "No"]]
Since Workshop 1, have you done any of the following? (Select all that apply)
[[Choices]]
Compared outputs across two or more LLMs
Checked an AI output against an authoritative source
Used the CRAFT lesson-prompt template
Shared what you learned with a colleague
Modified a lesson based on AI output
None of the above

[[Question:TE:Essay]]
[[ID:W1E3]]
[[DisplayLogic: W1_ATTEND != "No"]]
Briefly describe one thing you tried between W1 and W2. (Optional)
```

Then modify the existing *Workshop 2 — Knowledge and Confidence* block:

- Keep W2K1, W2K2, W2K3 (fix W2K1 anchor to "5 - Strong understanding"; fix W2K2 anchor to "1 - Cannot do this").
- Keep W2C1 as is.
- Reclassify W2C2 (academic integrity) to a new block *Workshop 2 — Ethics and Policy* to signal it is not a Fortify measure.

Then append a new block *CRAFT Cross-Workshop Anchor*:

```
[[Block:CRAFT Cross-Workshop Anchor]]

[[Question:MC:SingleAnswer:Horizontal]]
[[ID:ANCHOR_C1]]
How confident are you in using AI tools to support your STEM teaching?
[[Choices]]
1 - Not confident
2
3 - Somewhat
4
5 - Very confident

[[Question:MC:SingleAnswer:Horizontal]]
[[ID:ANCHOR_C2]]
How confident are you in identifying errors in AI-generated STEM content?
[[Choices]]
1 - Not confident
2
3 - Somewhat
4
5 - Very confident

[[Question:MC:SingleAnswer:Horizontal]]
[[ID:FORT1]]
How confident are you in comparing outputs from two or more LLMs on the same prompt to verify accuracy?
[[Choices]]
1 - Not confident
2
3 - Somewhat
4
5 - Very confident

[[Question:MC:SingleAnswer:Horizontal]]
[[ID:FORT2]]
How confident are you in cross-checking AI-generated claims against authoritative sources (textbooks, peer-reviewed articles, official curricula)?
[[Choices]]
1 - Not confident
2
3 - Somewhat
4
5 - Very confident

[[Question:MC:SingleAnswer:Horizontal]]
[[ID:FORT3]]
How confident are you in designing adversarial prompts to probe whether an AI output is reliable?
[[Choices]]
1 - Not confident
2
3 - Somewhat
4
5 - Very confident

[[Question:MC:SingleAnswer:Horizontal]]
[[ID:CRAFT_KNOW]]
How familiar are you with the CRAFT pedagogical cycle?
[[Choices]]
1 - Never heard of it
2 - Heard of it
3 - Can name some phases
4 - Can use in lesson planning
5 - Have taught with it
```

### W2 Post-Survey

Mirror the Pre additions (ANCHOR_C1, ANCHOR_C2, FORT1, FORT2, FORT3, CRAFT_KNOW) and add the W2-specific intent item:

```
[[Question:MC:SingleAnswer:Horizontal]]
[[ID:W2P1]]
How likely are you to systematically verify AI outputs (e.g., using cross-LLM comparison or the Check the Machine protocol) before using them in your classroom within the next month?
[[Choices]]
1 - Very unlikely
2
3 - Neutral
4
5 - Very likely
```

Do **not** repeat the W1-attendance/enactment block on Post. That is a Pre-only retrospective.

## 7. Open questions for you to decide

1. **Scope for April 18:** Option A (safe, fast) or Option B (substantive, IRB-dependent)?
2. **Academic-integrity item (W2C2):** reclassify to a separate Ethics block, or drop entirely in favor of the ANCHOR_C2 item, or keep alongside?
3. **Open-response R1/R2 on W2 Post:** the current R1 prompt ("one AI error you found today and how you verified it") is excellent Fortify data. Keep. R2 ("how will you implement Check the Machine") is also good. Keep.
4. **W3 cross-workshop anchor:** commit now to adding ANCHOR items to W3 Pre/Post (ties W3 into the longitudinal design), or defer pending W2 results?
5. **Delayed post-series survey:** begin IRB amendment conversation now, or wait until after W3?

## 8. Manuscript integration notes

If Option B is adopted, the manuscript should be updated minimally in two places before submission:

- **§4.3 Instruments:** Add a one-paragraph note that W2/W3 instruments include additional cross-workshop anchor items supporting the multi-session follow-up work described in §5.7. No reanalysis of the N=16 W1 data is required, since the manuscript's primary results are W1-only.
- **§5.7 Future Work:** Revise item (i) to reference the specific instrumentation now in place: "A multi-session follow-up in the same Noyce cohort (W2, April 2026) re-administers the C2 item and adds three Fortify sub-technique items, testing whether repeated Fortify practice closes the effect-size gap."

This is a strengthening edit, not a re-scope.
