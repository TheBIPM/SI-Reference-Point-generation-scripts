# Governance model for updating the SI Reference Point

(Description of the semantic version numbering, major - minor - patch)

## 1. Reception and registration of a request

Requests can be made by anyone in the community, in the form of a GitHub issue, an email, or verbal communication in meetings, among other ways. Some requests may respond to updates in reference documents (mainly the SI Brochure), may be reports of errors (bugs), or demands for new features.

The requests that are not received as a GitHub issue shall be registered in one of the public repositories.

> CP: How do we decide which issues go to which repository? Maybe knowledge-model-related to the [generation scripts repo](https://github.com/TheBIPM/SI-Reference-Point-generation-scripts) and web-services-related to the [SI Digital Framework repo](https://github.com/TheBIPM/SI_Digital_Framework)? Issues can be moved between public repositories and original links will redirect to the new locations.

Before opening a new issue, the issues pages of the public repositories are assessed for entries that already relate to the topic. If there is already an ongoing discussion, the new information is registered as a comment. On the contrary, a new issue is registered on behalf of the person who originally made the request, and the link is shared

> CP: Do we request consent to publish the issue (or comment) on behalf of the person?

All issues are automatically added to the backlog of the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) (in GitHub, with restricted access).

## 2. Assessment and prioritization

Anyone, whether an expert group member or not, can comment on any issue at any time.

The expert group meetings are convened by the BIPM. At every meeting, the participants assess the dashboard of the [SIRP update project page](https://github.com/orgs/TheBIPM/projects/6) that organizes the topics in different status fields. All issues are initially in status **Backlog**, meaning that it has been registered and may contain additional comments, but no decision has been made. The issues in backlog are discussed and may be assigned a new status depending on the consensus reached:

- **Planned**: The request is reasonable or necessary.
- **Consultation**: The expert group participants consider that the topic must be discussed at a different instance: the SIDF task group, a working group of the CIPM Forum on Metrology and Digitalization (FORUM-MD), the Consultative Committee of Units (CCU), another Consultative Committee of the BIPM.
- **Done**: The request tackles a topic that has already been solved or is a duplicate of another issue.
- **Not planned**: The request has been deemed unsuitable under current circumstances.

Before moving the status of any issue in the backlog, a comment is added with a summary of the discussion. In case the status is set to **Done** or **Not planned**, the issue is closed.

For issues moved to **Consultation**, ... ..., afterward, the issue may be moved to **Not planned** or to **Planned**.

For issues with status **Planned**, a prioritization level must be assigned (high, medium, low) and the impact of the implementation upon update is estimated (patch update, minor update, major update).

## 3. Branch creation and code development

## 4. Expert group review

## 5. Approval

### 5.1. Patch or minor update

Expert group decision, SIDF-TG informed

### 5.2. Major update SIDF-TG approval, CCU consulted

## 6. Merge and knowledge graph generation

## 7. Release

(previous version URIs remain dereferenceable)

## 8. Website update and announcement

## 9. Issue reporters notified of resolution
