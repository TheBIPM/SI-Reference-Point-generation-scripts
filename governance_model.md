# Governance model for updating the SI Reference Point
> *This document is in draft form.*
## Table of Contents
[1. Document objectives and scope](#1-document-objectives-and-scope)  
[2. General overview of the SI Reference Point](#2-general-overview-of-the-si-reference-point)  
[3. Stages for change requests of the SIRP](#3-stages-for-change-requests-of-the-sirp)  
[4. Version numbering scheme](#4-version-numbering-scheme)  
[5. Archiving of versions](#5-archiving-of-versions)  
[6. Change management](#6-change-management)


## 1. Document objectives and scope
This document specifies the governance model for the SI Reference Point (SIRP), a service developed and maintained under the auspices of the BIPM. It sets out how change requests and bug reports are processed, covering the full path from the initial change request to the release of an updated SIRP. It establishes labelling conventions for releases, principles for the development process and the review procedure before the update is released. It also defines the responsibilities and competences of the Expert Group of the Forum-MD-TG-SIDEF.  
The document does not describe the SIRP in full but only gives a short overview of the service. For a full description, please refer to XXXXX.

  
## 2. General overview of the SI Reference Point

The SI Reference Point (SIRP) is a machine-actionable knowledge model of the SI Brochure [(#ref)](http://doi.org/).
The SIRP is developed by the members of the Expert Group of the FORUM-MD Task Group on SI Digital Framework [TG-SIDF](https://www.bipm.org/en/committees/fo/forum-md/wg/forum-md-tg-sidf) under the auspices of the BIPM.  
The web services available at [https://si-digital-framework.org/SI](https://si-digital-framework.org/SI) provide access to the knowledge model of the SIRP.
The web services are developed by the BIPM, consulting with members of the Expert Group when considered necessary.

## 3. Stages for change requests of the SIRP
Changes of the SIRP respond to feedback received from the user community. Each request will go through stage 1,2 and 6. If it is decided to implement a change, it goes also through stages 3 to 5:

1.  Reception and registration of a request
2.  Classification, assessment and prioritization
3.  Development
4.  Review and approval
5.  Release
6.  Close the request

The individual stages are further described below.
A [diagram of the process](#diagram-of-the-process) is provided at the end of the document.

<a name="note1"></a>
> **Note:**
    The procedures stated in this governance document apply to requests related to the SIRP (the knowledge model).
    Issues related to the web services or to the management of the repository are handled by the BIPM staff, who may nonetheless choose to apply some of these procedures at their own discretion.

### 3.1 Reception and registration of a request
Change to the SIRP may become necessary after updates of reference documents (mainly the SI Brochure), to address an error in the knowledge base (bugs) or in response to a request for a new feature. Any change requests can be deposited directly by raising a GitHub issue, by sending an email to XXXX(administrator), or by verbal communication to a member of the Expert Group (e.g. during meetings). Every requests must be linked to a requester, either an individual or a body e.g. working group of a CIPM Consultative Committee. If a person submits a request on behalf of someone else, the information *on behalf* of should be included in the new issue.

Issues can be raised by
- users, directly on the GitHub repository
representatives of the corresponding digitalization working group of a CIPM Consultative Committee (label `request-from-CC`)
- a FORUM-MD working group (label `request-from-FORUM-MD`)
- a liaison organization (label `request-from-liaison-org`).

Requestors are encouraged to propose a label (see below) for the issue they raise. Adding information about the origin and the scope of the issue is useful when deciding the priority of the topics.

Requests that are not submitted  as a GitHub issue shall still be registered as GitHub issue in either of the two public repositories by a member of the Expert Group.  

Before opening a new issue, it should be checked if an existing open issue relates to the same topic. If there is a related issue, the new information should be added to the discussion as a comment. Where no related issue exists, a new issue should be registered.
<!-- For these purposes, the person raising the issue can be invited to use their GitHub account, but if this is not feasible, the person receiving the request can file the issue on their behalf.
In this case, a disclaimer shall be included (*On behalf of...*), and the link to the new issue (or to the comment) shall be shared with the person who originally submitted the request. -->


### 3.2 Classification, assessment and prioritization
Requests are managed in the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6), which provides a dashboard to follow up on the status of the requests.
The dashboard is accessible to members of the Expert Group.
View-only access can be granted to members of the Forum-MD-TG-SIDEF upon request.  

Every duly recorded issue must have three labels: a scope label, a priority label and a status label.

#### 3.2.1 Scope labels
The scope label helps to identify and to prioritize the issue. 

Issues are classified according to their scope (mandatory) from the list below <span style="color:red">is this list exhaustive? </span> and complemented with information about the origin of the issue (requestor). If no information is provided by the initial author, the **administrator** will consult with the inital author to ascribe a scope. 

Possible scope lables
| Issues related to| Label          | 
|:-------|:--------:|
| Ontology| `scope-ontology` |
| Web services | `scope-web-services`|
| Management of the repository| `scope-repo-management` |
| Python package, not causing any effect on the ontology itself| `scope-python-package` |
| Questions that do not require any changes| `scope-question` |

<a name="note2"></a>
> **Note:**
    The issue of the last type (Questions) can be closed immediately after an answer has been provided.
#### 3.2.2 Priority label    
Priority labels give an indication how urgently an issue should be resolved. 
The Expert Group assesses an prioritize issues related to the knowledge model. (see the [note](#note1) above).
Possible priority lables
| Priority | Label          | 
|:-------|:--------|
| low | `priority-low` |
| medium | `priority-medium` |
| high | `priority-high` |

#### 3.2.3 Status label
The status label helps to track the progress being made with a specific issue. At every meeting of the Expert Group the issues in the dashboard of the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) are discussed and reorganized in status boxes:
 <span style="color:red">above it is said that request can be deposited in both repositories. Shouldn't we combine the request in a single repo? Maybe this is was is meant below under `Backlog: manually imported` </span>

- [<ins>Backlog</ins>](#backlog)
- [<ins>Planned</ins>](#planned)
- [<ins>Consultation</ins>](#consultation)
- [<ins>In progress</ins>](#in-progress)
- [<ins>In review</ins>](#in-review)
- [<ins>Awaiting release</ins>](#awaiting-release)
- [<ins>Done</ins>](#done)
- [<ins>Not planned</ins>](#not-planned).  

The meaning of each status is described below.

<div style="padding-left: 50px; padding-right: 50px;" markdown="1">

---
#### Backlog
Every issue starts here, meaning that it has been registered and may contain additional comments, but no decision on prioritization or implementation has been made.
The issues registered in the repository [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) are added automatically to the [<ins>Backlog</ins>](#backlog), while those registered in the repository [TheBIPM/SI_Digital_Framework](https://github.com/TheBIPM/SI_Digital_Framework) must be imported manually.
Optionally, issues from other private repositories (e.g. related to the web services) can be added here to ease the follow-up of topics.

The issues in the [<ins>Backlog</ins>](#backlog) are discussed during the meetings of the Expert Group and may thereafter be assigned the status [<ins>Planned</ins>](#planned), [<ins>Consultation</ins>](#consultation), or [<ins>Not planned</ins>](#not-planned), depending on the conclusion from the participants in the meeting.
Before moving any issue from this box, a comment is added with a summary of the outcomes of the discussion.

---
#### Planned
This status is assigned to requests from the [<ins>Backlog</ins>](#backlog) that have been considered feasible  and necessary by the Expert Group members.
This status may also be assigned to requests previously in [<ins>Consultation</ins>](#consultation), depending on the feedback that was collected from another body.

Issues here are assigned the label `status-planned`, meaning that the Expert Group members undertake to advance them in due time.

A priority level must be defined by Expert Group members.
The decision is made explicit by adding one of the labels `priority-high`, `priority-medium` or `priority-low`.
Depending on the prioritization and complexity level of the issue, one or more Expert Group members may volunteer to work on the code implementation depending on their availability and area of expertise.
This delegation is declared on the webpage of the issue using the GitHub function *Assignees*.

The impact of implementing the solution to the issue shall be estimated, according to the following update types adapted from the [Semantic Versioning scheme](https://semver.org/):
- `possible-update-major`:
    A change will introduce incompatibility with former versions of the knowledge model (e.g. eliminating a class, renaming a datatype property).
- `possible-update-minor`:
    A feature will be introduced in a backward-compatible manner (e.g. adding new individuals, like new units of measurement).
- `possible-update-patch`:
    A bug will be fixed in a backward-compatible manner (e.g. fixing a comment or relabelling an individual).

Changes that will likely involve a major version update must be discussed and approved at the TG-SIDF, which might decide to further discuss the implications with other groups of the FORUM-MD or a CIPM Consultative Committee (see Section [4. Review and approval](#4-review-and-approval)).
The label for the possible type of update can be modified during the development of the solution to a request.

When the code implementation is ready to begin, the issue is moved to the status [<ins>In progress</ins>](#in-progress).

---
#### Consultation
This status is assigned to requests from the [<ins>Backlog</ins>](#backlog) that the Expert Group considers must be discussed by a higher body because it implies a high-level decision, or because there is strong disagreement among the Expert Group members regarding the suitability of the request.

Issues here are assigned the label `status-consultation`, meaning that the Expert Group members undertake to discuss the issue externally to make a decision.

The default body to consider for consultation is the TG-SIDF, but the Expert Group members can also decide to discuss the topic directly with another working group of the FORUM-MD, the Consultative Committee for Units (CCU), or another Consultative Committee of the CIPM.
At least one Expert Group member must be designated as responsible for doing the consultation.
When the information has been gathered, a summary must be added as a comment to the issue webpage.
After discussing the newly collected information, the issue can be assigned the status [<ins>Planned</ins>](#planned) or [<ins>Not planned</ins>](#not-planned).

---
#### In progress
This status is assigned to issues marked [<ins>Planned</ins>](#planned) once some Expert Group members decide to start working on the code implementation to address them.

Issues here are assigned the label `status-in-progress`, meaning that the solution to the request is being advanced. 

The details of this stage are given in Section [3. Development](#3-development).
When the code implementation is considered finished, the issue is assigned the status [<ins>In review</ins>](#in-review).

---
#### In review
This status is assigned to issues marked [<ins>In progress</ins>](#in-progress) once the people working on a request consider that the code implementation is complete.

Issues here are assigned the label `status-in-review`, meaning that a solution to a request has been proposed and it is being evaluated either by the Expert Group or at a higher body.

The details of this stage are given in Section [4. Review and approval](#4-review-and-approval).
Depending on the outcome of the review, the issue can be moved back to status [<ins>In progress</ins>](#in-progress), or advanced to status [<ins>Awaiting release</ins>](#awaiting-release).

---
#### Awaiting release
This status is assigned to issues marked [<ins>In review</ins>](#in-review), after the designated body has approved the changes.

Issues here are assigned the label `status-awaiting-release`, meaning that the request was addressed and the changes will be published in the next release of the SIRP.

The details of this stage are given in Section [5. Release](#5-release).
After the release has been done, the issue is advanced to the latest status [<ins>Done</ins>](#done).

---
#### Done
This status is achieved to issues that were marked [<ins>Awaiting release</ins>](#awaiting-release), after the updated knowledge model of the SIRP has been released.
The issues moved to this status box can be closed as completed and the person who originally made the request is notified.

---
#### Not planned
This status is assigned to issues from the boxes [<ins>Backlog</ins>](#backlog) or [<ins>Consultation</ins>](#consultation), when the corresponding decision body has considered them unsuitable under current circumstances.
The person who originally made the request is notified about the decision not to proceed with the request, with a summary of the reasons considered.

The issues here are assigned the label `status-not-planned` and must be closed (GitHub function *Close as not planned*) on the issue webpage.

---
</div>




### 3.3 Development
The development is done in the repository [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts).
This section describes the guidelines for branching and merging.

#### 3.3.1. Branching
The repository will always hold two permanent branches: 

* Branch `origin/main`:
    Always reflects the version of the Python package that generates the latest stable release of the SIRP, available both on the [website of the SI Digital Framework](https://si-digital-framework.org/) and in the [read-only repository of the SI Digital Framework](https://github.com/TheBIPM/SI_Digital_Framework).
* Branch `origin/develop`:
    Contains the latest feature implementations and bug fixes that have been approved for the next release of the SIRP.

To start working on an issue that was [<ins>Planned</ins>](#planned), a member of the Expert Group creates a branch (feature branch) that will have a limited lifetime.
The feature branches are created from the branch `origin/develop` and should be named in an informative way, including the number of the issue when possible.
For example, a good name for the [issue #95](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts/issues/95) that relates to version 4.01 of the 9th edition of the SI Brochure could be `95-new-version-of-the-9th-edition-of-the-si-brochure-v4_01`.
A single feature branch can be used to work on more than one issue.
The URL of the feature branch must be referenced in the webpage of the issues, either automatically by a GitHub workflow, or manually in a comment by the person creating the branch.

The issues that have an active branch should be assigned the status [<ins>In progress</ins>](#in-progress).

Before pushing modifications to the code in the repository, it is encouraged to verify that changes are being pushed to the correct branch by running the command `git status`.
Additionally, it is highly encouraged to merge the changes from the branch `origin/develop` into the feature branch frequently, to avoid conflicts when the feature branch is eventually merged back.

#### 3.3.2. Contributions from outside the Expert Group
Members of the broader community who do not have write access to the repository can still contribute by first creating a fork of [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) under their own GitHub account.
Feature branches are then created within this fork, following the same conventions described in Section [3.3.1. Branching](#331-branching).
Once the proposed changes are ready, a pull request can be opened from the forked branch into the `origin/develop` branch of the main repository, as described in Section [3.3.3. Opening a pull request](#333-opening-a-pull-request).

#### 3.3.3 Opening a pull request
When the code patch that addresses a request is considered finished by the people involved, they shall request to merge the changes from the feature branch (in a forked repository in the case of external contributors), into the branch `origin/develop`.
All merging conflicts must be resolved before creating a pull request.
The URLs of the issues that are tackled by a pull request shall be mentioned in the pull request message or in a comment to the pull request.

Issues that have an active pull request should be assigned the status [<ins>In review</ins>](#in-review).

### 3.4. Review and approval
Every pull request to branch `origin/develop` is initially reviewed by BIPM staff.
The changes must be assessed thoroughly to confirm that their implementation does not introduce a backward-incompatible change.
This assessment should consider potential effects on other BIPM digital services that rely on the SIRP, like the Key Comparison Database (KCDB).
The label of the possible kind of update associated with an issue may change as a consequence of this assessment.


#### 3.4.1. Issues labelled as `possible-update-minor` and `possible-update-patch`
After confirming that the changes maintain backward compatibility,

 >*__Here we need to decide on one of the following approaches__*

|*Option 1: Direct approval by BIPM staff*| *Option 2: Notice period before approval*|
|---|---|
|The pull request is approved at BIPM staff's discretion, with further consultation with other members of the Expert Group when considered necessary. The change is notified to all members of the Expert Group by email on a regular basis, including the links to the corresponding pull request. The Expert Group members are encouraged to comment on the closed pull request. In case of unresolved disagreement, the discussion is held at the Expert Group meetings.  | Expert Group members are informed by email of open pull requests. They are encouraged to comment in case of suggestions or disagreement. After a period of at least seven calendar days, the pull request can be approved by BIPM staff.|

All changes to the branch `origin/develop` can be reverted in case it is considered necessary.

The issues for which a pull request has been merged to the branch `origin/develop` should be assigned the status [<ins>Awaiting release</ins>](#awaiting-release).
If the changes are not approved, the feature branch is not merged, and the issue is returned to [<ins>In progress</ins>](#in-progress).


#### 3.4.2. Issues labelled as `possible-update-major`
The outcome of the changes that imply a major update of the knowledge model should be discussed at the TG-SIDF meeting.
The implications of the changes may be discussed with other working groups of the FORUM-MD, or with other CIPM Consultative Committees. 
If the changes are approved, the feature branch is merged into the branch `origin/develop`, and the issues are assigned the status [<ins>Awaiting release</ins>](#awaiting-release).
The communities that may be affected by the major update shall be notified accordingly.
If the changes are not approved, the feature branch is not merged, and the issue is returned to [<ins>In progress</ins>](#in-progress).

### 3.5. Release
After the approval of the update is done at the corresponding body, the release of the updated version of the SIRP includes the following steps:

1.  Assignment of a version number.
2.  Drafting of release notes, summarizing the changes made to the knowledge model since the latest release.
3.  Circulation of the release notes to the TG-SIDF members by email, along with the updated knowledge model serialized as Turtle files.
4.  A period of seven calendar days is given to raise any objections regarding the update of the knowledge model.
5.  If there are no objections, the changes in branch `origin/develop` are merged into the branch `origin/main`.
    If there are objections, the comments may be addressed and the amendments circulated again for consultation to the TG-SIDF members, or should be further discussed at the following meeting of the TG-SIDF.
6.  A GitHub release is done in the [generation scripts repository](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) including the files of the knowledge model, serialized both as Turtle and JSON-LD formats, in the field for *binaries*.
7.  The Turtle files are updated in the [SI Digital Framework repository](https://github.com/TheBIPM/SI_Digital_Framework).
8.  The web services of the [SI Digital Framework website](https://si-digital-framework.org/) are restarted with the updated SIRP.
9.  A successful release is indicated to the community by using the BIPM communications channels, as considered appropriate by the TG-SIDF chair.
10. The people whose requests were satisfied with the release of the SIRP are notified.

Previous versions of the SIRP remain accessible by using the version URIs.
The canonical URLs (without version number) resolve to the latest released version of the SIRP.

## 4. Version numbering scheme
Releases of the SIRP are versioned according to the [Semantic Versioning scheme](https://semver.org/), using three dot-separated integer numbers known as the major, minor and patch version (see [below](#planned)).

## 5. Archiving of versions
The project is handled at two public GitHub repositories that serve different purposes:

- [TheBIPM/SI-Reference-Point-generation-scripts](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts):
    A Python package that generates the knowledge graph of the SIRP serialized as Turtle and JSON-LD files.
- [TheBIPM/SI_Digital_Framework](https://github.com/TheBIPM/SI_Digital_Framework):
    A read-only repository to track changes in the Turtle-serialized files of the SIRP and other related ontologies published by the BIPM.

## 6. Change management
Changes to procedure of this document must be approved by the Forum-MD-TG-SIREF
| Date | Change          | 
|:-------|:--------:|
| 2026-10-18 | Initial version, approved by Forum-MD-TG-SIREF on XXXXX |




## Diagram of the process
``` mermaid
flowchart TB
    REQ["Request received<br>GitHub issue, email, meeting"] --> DUP{"Related issue<br>already open?"}
    DUP -- Yes --> CMT["Add comment to existing issue"]
    DUP -- No --> NEW@{ label: "Register new issue.<br>Add *'On behalf of…'* if needed" }
    CMT --> BL["`**Backlog**<br>Classify: scope (mandatory),<br>requesting body (optional)`"]
    NEW --> BL
    BL --> EG{"Expert Group<br>meeting"}
    BL -- label 'question' --> QA["Answer and close"]
    EG -- Feasible & necessary --> PL["`**Planned**<br>Priority label, assignees,<br>possible-update-major/minor/patch`"]
    EG -- Unsuitable --> NP["`**Not planned**<br>Notify requester with reasons,<br>close as not planned`"]
    EG -- "High-level decision needed <br>or strong disagreement" --> CO["`**Consultation**<br>TG-SIDF, FORUM-MD WG,<br>CCU or other CC`"]
    CO -- Findings: unsuitable --> NP
    CO -- Findings: approved ---> PL
    PL -- Feature branch from develop --> IP["`**In progress**`"]
    IP -- Pull request to develop --> IR["`**In review**<br>BIPM staff check backward<br>compatibility, KCDB impact`"]
    IR --> IMP{"Impact?"}
    IMP -- Minor / patch --> BS{"BIPM staff<br>approval?"}
    IMP -- Major --> TG{"TG-SIDF<br>approval?"}
    BS -- No --> IP
    TG -- No --> IP
    BS -- Yes: merge to develop --> AR["`**Awaiting release**`"]
    TG -- Yes: merge to develop,<br>notify affected communities --> AR
    AR --> RN["Version number, release notes,<br>circulate to TG-SIDF with Turtle files"]
    RN --> OBJ{"Objections within<br>7 calendar days?"}
    OBJ -- Yes --> AC["Address comments<br>Expert Group or TG-SIDF meeting"]
    AC --> RN
    OBJ -- No --> PUB["Merge develop → main<br>GitHub release (Turtle + JSON-LD)<br>Update SI_Digital_Framework repo<br>Restart web services, announce"]
    PUB --> DN["`**Done**<br>Close issue, notify requester`"]

    NEW@{ shape: rect}
     BL:::status
     QA:::terminal
     PL:::status
     NP:::reject
     CO:::status
     IP:::status
     IR:::status
     AR:::status
     DN:::terminal
    classDef status fill:#e8f0fe,stroke:#1a56db,stroke-width:2px
    classDef terminal fill:#e6f4ea,stroke:#137333,stroke-width:2px
    classDef reject fill:#fce8e6,stroke:#c5221f,stroke-width:2px
```
