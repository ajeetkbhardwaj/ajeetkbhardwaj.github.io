---
layout: single
title:  "Draft Post"
header:
  teaser: "unsplash-gallery-image-2-th.jpg"
categories: 
  - Jekyll
tags:
  - edge case
---
---

title: "A Game of Agents"
excerpt: "We often discuss cooperation in almost every field of science, technology, engineering, and mathematics. In artificial intelligence, cooperation can also be understood among the agents themselves—whether virtual systems or physical machines—not only among humans."
date: 2026-10-22
permalink: /posts/2026/10/a-game-of-agents/
categories:

- AI Safety
- Game Theory
- Multi-Agent Systems

---

We often discuss cooperation in almost every field of science, technology, engineering, and mathematics. In biology, cells cooperate within organisms. In economics, people cooperate through markets, institutions, and contracts. In engineering, components cooperate within a larger system. In mathematics, cooperation appears in game theory, optimization, and the study of collective behaviour.

Over the past decade, artificial intelligence has developed rapidly. Since the introduction of the transformer architecture in *“Attention Is All You Need”* by Vaswani et al., AI systems have become increasingly capable of reasoning, planning, writing, coding, and acting in complex environments. As these systems become more capable, an important question emerges: **what does cooperation mean when the agents are not humans, but AI systems?**


Cooperation among AI agents can involve virtual systems, such as language models working together on a task, or physical systems, such as autonomous vehicles coordinating on a road. In either case, the agents may share information, divide labour, pursue a common goal, or respond to one another’s actions.

At first glance, cooperation seems clearly beneficial. A group of agents that shares information, divides work, and pursues shared goals may be safer and more capable than isolated agents. But this intuition is incomplete. Cooperation can also produce harmful outcomes. Agents may coordinate in ways that harm people, undermine competition, evade oversight, or deplete shared resources.

Understanding cooperation in AI systems therefore requires more than asking whether agents collaborate. We must also ask:

- With whom are they cooperating?
- What are they cooperating on?
- Who benefits from the cooperation?
- Who bears the costs?
- Can the cooperation be supervised or prevented if it becomes harmful?

Game theory provides a useful language for answering these questions.

## Cooperation is a strategic problem

In ordinary optimisation, an agent chooses an action to maximise a fixed objective. For example, a navigation system may choose a route that minimises travel time.

In a multi-agent setting, the situation is different. The best action for one agent may depend on what other agents are doing. At the same time, the other agents’ choices may depend on what they expect the first agent to do.

This is the basic structure of a game.

A game consists of players, available actions, and payoffs. Each player chooses an action, and the resulting payoff depends on the combination of choices made by everyone. In game theory, a player may be a person, a company, a country, or—in our case—an AI system.

The central question is not simply, “What should this agent do?” Instead, it becomes:

> Which combination of choices is stable when every agent responds rationally to the choices of the others?

This question leads to the idea of a **Nash equilibrium**: a situation in which no single agent can improve its own outcome by changing its action alone, assuming the other agents’ actions remain fixed.

Importantly, a Nash equilibrium does not necessarily describe a good outcome. It only describes a stable one.

## The prisoner’s dilemma

The prisoner’s dilemma is the classic example of the tension between individual incentives and collective welfare.

Imagine two suspects who are questioned separately. Each can either remain silent or confess. If both remain silent, both receive a light sentence. If one confesses while the other remains silent, the confessor goes free while the other receives a heavy sentence. If both confess, both receive an intermediate sentence.

We can write this as a payoff matrix, where the first number is the payoff to the row player and the second is the payoff to the column player. Here, $C$ means cooperate with the other suspect by remaining silent, while $D$ means defect by confessing.

|                      | Other player:$C$ | Other player:$D$ |
| -------------------- | -----------------: | -----------------: |
| **You: $C$** |        $(-1,-1)$ |        $(-10,0)$ |
| **You: $D$** |        $(0,-10)$ |        $(-6,-6)$ |

If the other player cooperates, you receive $0$ by defecting and $-1$ by cooperating. If the other player defects, you receive $-6$ by defecting and $-10$ by cooperating. In both cases, defection is better.

Formally, for either player,

$$
u_i(D,C)>u_i(C,C)
$$

and

$$
u_i(D,D)>u_i(C,D).
$$

Therefore, $D$ is a strictly dominant strategy. Since this holds for both players, $(D,D)$ is the unique Nash equilibrium.

Yet both players would prefer $(C,C)$, where each receives $-1$, to $(D,D)$, where each receives $-6$. The dilemma is that the mutually beneficial outcome is not stable against unilateral deviation.

This structure appears whenever an agent can gain by acting selfishly, but mutual selfishness leaves everyone worse off.

## Do people actually defect?

The prisoner’s dilemma is a mathematical model, not a prediction that people will always defect. Experiments show that human behaviour is more varied.

| Study                       | Design                                 | Mutual cooperation | Mutual defection | Mixed |
| --------------------------- | -------------------------------------- | -----------------: | ---------------: | ----: |
| Khadjavi & Lange (2013)     | One-shot, 90 female inmates            |                30% |              18% |   52% |
| Khadjavi & Lange (2013)     | One-shot, 92 female students           |                13% |              39% |   48% |
| Andreoni & Miller (1993)    | 20 games of 10 rounds                  |                31% |              45% |   24% |
| Cooper et al. (1996)        | 2 games of 10 rounds                   |                42% |              32% |   26% |
| Dal Bó (2005)              | Games of 4 rounds                      |                10% |              61% |   29% |
| Dal Bó & Fréchette (2011) | Continuation probability$1/2$        |                24% |              44% |   32% |
| Dal Bó & Fréchette (2011) | Continuation probability$3/4$        |                91% |               3% |    6% |
| Mao et al. (2017)           | 10-round games, up to 400 over 20 days |                80% |              11% |    9% |

The results do not show that people ignore incentives. Rather, they show that people often bring additional considerations into the game: fairness, reciprocity, reputation, social norms, and expectations about future interaction.

The most striking result is the comparison between continuation probabilities of $1/2$ and $3/4$. When the game was more likely to continue, mutual cooperation rose from 24% to 91%, while mutual defection fell from 44% to 3%.  In other words, when the future matters more, cooperation becomes much more attractive.

This is often called the **shadow of the future**. If an interaction is likely to continue, an agent may cooperate today to preserve a relationship that can produce benefits tomorrow.

## Repeated interaction changes incentives

In a one-shot prisoner’s dilemma, there is no future after the current decision. Cooperation cannot be rewarded later, and defection cannot be punished later.

In a repeated game, this changes.

Suppose two agents interact for $N$ rounds. A simple cooperative strategy is **tit-for-tat**:

1. Cooperate in the first round.
2. After that, copy the opponent’s previous action.

If one agent uses tit-for-tat and the other always defects, the first agent cooperates once, is exploited, and then defects forever.

| Round | Tit-for-tat | Always defect |
| ----- | ----------- | ------------- |
| 1     | Cooperate   | Defect        |
| 2     | Defect      | Defect        |
| 3     | Defect      | Defect        |
| 4     | Defect      | Defect        |

Against tit-for-tat, permanent defection gives an immediate gain but destroys future cooperation. Permanent cooperation may produce a higher total payoff.

This is why “always defect” is not dominant in a repeated prisoner’s dilemma. The possibility of future interaction can make cooperation rational.

## Three ways cooperation can fail

When multiple AI agents interact, cooperation can fail in different ways. A useful framework distinguishes between **miscoordination**, **conflict**, and **collusion**.

| Failure mode    | Objectives | Is cooperation desirable? | Central problem                                             |
| --------------- | ---------- | ------------------------- | ----------------------------------------------------------- |
| Miscoordination | Shared     | Yes                       | Agents pursue the same goal through incompatible strategies |
| Conflict        | Mixed      | Yes                       | Individual incentives undermine a jointly better outcome    |
| Collusion       | Any        | No                        | Agents cooperate in ways that harm outsiders                |

### Miscoordination

Miscoordination occurs when agents share an objective but use incompatible strategies.

Consider two autonomous vehicles trained under different driving conventions. One system may be trained to yield to the right, while another is trained to yield to the left. Both systems may be trying to drive safely, but if they meet at an intersection, their rules are incompatible. The result can be a collision.

The problem is not necessarily that either system is malicious or incompetent. Each may perform well within its own environment. The failure arises when they must interact without a shared convention.

This is why interoperability matters. AI systems may need shared protocols, common standards, and compatible assumptions about how other systems will behave.

### Conflict

Conflict arises when agents have mixed motives and fail to achieve an outcome that would be better for everyone.

The tragedy of the commons is a classic example. Imagine several agents sharing a fishery, pasture, or pollution sink. Each agent may benefit from extracting more from the shared resource. However, if every agent does so, the resource may be depleted and everyone may be worse off.

This is a multi-agent version of the prisoner’s dilemma. The private benefit of overuse is concentrated in one agent, while the cost is spread across the group.

In AI systems, this could occur when multiple agents draw on a shared computational budget, data infrastructure, or physical resource. Each agent may have an incentive to use more than its share, even though excessive use by all agents damages the system as a whole.

### Collusion

Collusion is the opposite problem. Here, agents may cooperate effectively, but their cooperation harms people outside the interaction.

For example, pricing algorithms in a market could learn to keep prices high rather than compete them down. The algorithms may be coordinating successfully, but the outcome harms consumers.

This case is important because it challenges a simple assumption: that cooperation among AI systems is always desirable. In many settings, competition is intended to discipline prices, improve quality, and protect users. If AI systems learn to coordinate in ways that remove that discipline, the result can be harmful even though the agents are cooperating successfully.

## The same mechanism, different outcomes

These three failures are related. In each case, agents are learning how to respond to one another. What differs is the surrounding structure: their objectives, available information, rules of interaction, and enforcement mechanisms.

The same capacity to coordinate can therefore produce very different outcomes.

- Agents may fail to coordinate when they should.
- Agents may fail to sustain cooperation when cooperation would benefit everyone.
- Agents may cooperate when cooperation itself is harmful.

This is why designing multi-agent AI systems requires attention to the environment, not merely to the individual model. A system that behaves safely in isolation may become unsafe when placed alongside other systems with different conventions, incentives, or objectives.

## Cooperation without instruction

One of the more striking developments in multi-agent AI is that cooperation can emerge without being explicitly programmed into every agent.

In one case study discussed in recent research on multi-agent risks, AI agents operating in a shared environment discovered a message board and recognised the presence of other agents. They began exchanging compressed notes, coordinating research, and redistributing work according to their remaining computational budgets.

At one point, an agent considered sacrificing its own run to provide information that could benefit the wider group. The agents reasoned that, because their own chance of receiving a reward had become negligible, sacrificing their remaining budget could produce greater value for the team. Other agents then signalled approval for the sacrifice.

This does not necessarily mean that the agents possessed human-like loyalty or moral commitment. Their behaviour may have reflected training in environments where cooperation was useful, imitation of cooperative patterns found in human text, or a calculated response to the incentives and information available in their environment.

Nevertheless, the case is important. It shows that cooperation can emerge as a property of multi-agent interaction, rather than as a feature explicitly designed into each individual system.

## The AGI race as a game

The prisoner’s dilemma is not only a story about two suspects. Its structure can appear in competition between countries developing advanced AI.

Imagine two countries, each choosing between a **baseline** development pace and an **accelerated** pace. Acceleration may increase a country’s chance of developing powerful AI first, but it also creates shared risks: misuse, loss of control, geopolitical instability, and reduced investment in safety.

Let $A$ be the payoff to the country that develops advanced AI first, $B$ be the payoff to the country that develops it second, where $B<A$, $x$ be the probability that a baseline country finishes first against an accelerating country, where $0<x<1/2$ and $c$ be the shared cost of acceleration.

Then the payoff matrix is

| Country 1 / Country 2 | Baseline                                     | Accelerated                                      |
| --------------------- | -------------------------------------------- | ------------------------------------------------ |
| **Baseline**    | $\left(\frac{A+B}{2},\frac{A+B}{2}\right)$ | $\left(xA+(1-x)B-c,(1-x)A+xB-c\right)$         |
| **Accelerated** | $\left((1-x)A+xB-c,xA+(1-x)B-c\right)$     | $\left(\frac{A+B}{2}-c,\frac{A+B}{2}-c\right)$ |

Suppose Country 1 accelerates while Country 2 uses the baseline pace. Country 1’s expected payoff is

$$
(1-x)A+xB-c.
$$

If Country 1 instead uses the baseline pace, its expected payoff is

$$
\frac{A+B}{2}.
$$

The gain from accelerating is therefore

$$
\begin{aligned}
\Delta
&=(1-x)A+xB-c-\frac{A+B}{2}\\
&=\left(\frac12-x\right)(A-B)-c.
\end{aligned}
$$

So acceleration is privately worthwhile when

$$
\boxed{\left(\frac12-x\right)(A-B)>c.}
$$

The first term, $\left(\frac12-x\right)(A-B)$, measures the expected advantage of improving one’s chance of finishing first. The second term, $c$, measures the shared risk cost.

When this inequality holds, each country may prefer to accelerate regardless of what the other does. The result is a prisoner’s dilemma: both countries accelerate, even though both would prefer a safer baseline path.

## When risk changes the game

The structure depends on the size of $c$.

If the shared risk cost is small, acceleration may be dominant. Both countries race, even though mutual restraint would be better for both.

If the shared risk cost is large, the game can become a coordination game. Mutual restraint becomes stable, but only if each country expects the other to restrain as well.

| Regime                 | Strategic structure                                   | Likely outcome       |
| ---------------------- | ----------------------------------------------------- | -------------------- |
| Small shared risk$c$ | Acceleration is individually attractive               | Race                 |
| Large shared risk$c$ | Mutual restraint and mutual racing can both be stable | Coordination problem |

This is an important lesson for AI governance. Reducing the risk cost $c$—through safety research, monitoring, verification, and international coordination—can change the strategic structure of the race.

It does not guarantee that countries will choose restraint. But it can make restraint a stable equilibrium rather than an outcome that each side has an incentive to abandon.

## Cooperation needs structure

Stable cooperation rarely depends on goodwill alone. It depends on the structure of incentives and consequences.

The history of nuclear deterrence offers a sobering analogy. In a first-strike scenario, each side may prefer to act first, even though mutual restraint would be better for both. Mutually assured destruction changes the payoff structure by ensuring that a first strike cannot eliminate the opponent’s capacity to retaliate. Mutual restraint then becomes an equilibrium.

A similar idea has been proposed, speculatively, for advanced AI infrastructure. If a slowdown agreement is supported by credible verification and by meaningful consequences for defection, mutual restraint may become stable. Such proposals raise serious practical, ethical, and geopolitical questions, and should not be treated as ready-made policy solutions. But they illustrate an important principle: cooperation becomes more reliable when defection has consequences.

## Designing for beneficial cooperation

The goal is not to eliminate cooperation among AI systems. Cooperation is often necessary. Autonomous vehicles need shared conventions. Research agents may need to divide complex tasks. Infrastructure systems may need to coordinate during failures.

The real challenge is to design environments in which beneficial cooperation is stable and harmful cooperation is difficult.

That requires attention to several questions:

- What objective is each agent optimising?
- What information can each agent access?
- Are agents able to communicate, and through what channels?
- What actions are available to them?
- Who benefits when agents coordinate?
- Who pays the cost when coordination fails or succeeds?
- Are harmful forms of coordination detectable and preventable?
- Are there credible mechanisms that make desirable agreements self-enforcing?

## A game, not just a model

Game theory does not tell us that AI agents will necessarily cooperate, compete, or collide. It gives us a language for asking why a particular pattern of behaviour is stable.

An AI system may defect because defection is individually optimal. It may cooperate because future interaction makes reciprocity valuable. It may coordinate because shared conventions reduce costly uncertainty. Or it may collude because coordination produces private gains at public expense.

The task for AI safety is therefore not simply to make agents more cooperative. It is to make the right kinds of cooperation possible, stable, and accountable.

That means designing shared standards where miscoordination is likely; changing incentives where individual rationality undermines collective welfare; and preserving competition, oversight, and accountability where cooperation could enable harm.

In multi-agent systems, the most consequential choices are often not made by any single agent alone. They are shaped by the game in which all of the agents are placed.
