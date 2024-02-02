---
layout: default
title: Research
header: none
permalink: /research/
---

{:.alert .alert-warning}
🔬 Let's break some systems together!
Our potential research directions are listed on this page for your reference.
Please reach out to us at EMAIL for further details.
Also, feel free to BYOI (Bring Your Own Ideas) - your input is highly valued!

## General direction

![img](/assets/img/direction.png)

---

### Target: Cyber-Physical Systems (CPS)

* Lead: Prof. Seulbae Kim
* Subject systems: robots, drones, autonomous vehicles, satellites, ...

###### 1. Verification of logic/algorithm implementation
* Key question: Are there any discrepancies between the intended
logic/algorithm and the actual software implementation?
* Reference:
  [RoboFuzz](https://seulbae-security.github.io/pubs/robofuzz-fse22.pdf),
  [DriveFuzz](https://seulbae-security.github.io/pubs/drivefuzz-ccs22.pdf)

###### 2. Tailoring automated software testing techniques for distributed CPS codebases
* Key question: Can we tailor existing testing techniques/metrics
to CPS codebases that are designed as distributed systems?

###### 3. Policy and testing methodologies for live/production systems
* Key question: How to guarantee safety of production systems during tests?

###### 4. Analysis/discovery of physical attack vectors
* Key question: Can we systematically attack the software (or the entire cyber-physical system)
through physical attacks?
* Reference:
  [Acoustic attack](https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-son.pdf)

###### 5. Creative attacks on sensor and perception layers
* Key question: How can we (silently) fool the eyes and brain of a cyber-physical system
to (maliciously) affect its behavior?
* Reference: [Frustum attack](https://www.usenix.org/system/files/sec22-hallyburton.pdf)

###### 6. Resource-constrained testing
* Key question: Many CPS have limited computing power and memory. Can we
quickly reveal issues associated when these resources are scarce?

###### 7. Cyber-physical security by design
* Key question: Can we carefully design the components of CPS to guarantee security?
(e.g., by having secure channel between the hardware and software)

###### 8. Exploring (the imperfectness of) physics simulators
* Key question: Three-dimensional physics simulators are widely used for
robotic development and testing. Are there any potential caveats caused by the flaws of the simulators?

---

### Target: Operating Systems and Large Software Systems

* Lead: Prof. Seulbae Kim
* Subject systems: Linux/Windows Kernel, web browsers, ...

###### 1. Automatically identifying non-memory issues (e.g., performance deradation)
* Key question: How to design test oracles and testing methodologies for the issues
that do not readily manifest (e.g., performance degradation)?

###### 2. Efficiently testing emulated systems
* Key question: Emulation comes at a cost of (terrible) performance.
Can we somehow skip the slow part for testing purposes?

###### 3. Improving fuzzing methodologies
* Keywords: Directed fuzzing, AI-assisted fuzzing, in-memory fuzzing, ...

###### 4. Automated Game testing
* Reference: [Towards automated video game testing: still a long way to go](https://dl.acm.org/doi/abs/10.1145/3524494.3527627)


---

### Target: AI/ML security
* Lead: Prof. Sangdon Park

<!-- TODO: sangdon -->
