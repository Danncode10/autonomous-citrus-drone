# Business Model: Citrus Orchard Intelligence

## Core idea

We are not primarily selling a drone. We are selling reliable, per-tree and per-block citrus intelligence that helps farms estimate harvest volume, plan labor, and make better production decisions.

The customer-facing offer should be described in plain language:

> Drone-based citrus monitoring, fruit-count estimates, and orchard mapping.

"Robotics as a Service" (RaaS) is an appropriate term for investors, partners, and technical audiences, but it should not be the main sales language used with farmers.

## Initial market

Start with Perante orange orchards in Nueva Vizcaya. This creates a defensible local advantage through crop-specific data, local relationships, and field experience.

The first ideal customers are not every small farmer. They are:

- Commercial orchards with a meaningful number of trees or blocks
- Cooperatives that can serve multiple growers
- Farms with a designated technician or operations staff member
- LGUs, agricultural offices, universities, and research farms that need monitoring data
- Buyers, traders, or exporters that benefit from earlier supply visibility

## The customer outcome

The product must answer questions that are worth paying for:

- What is the visible fruit-count estimate for this tree, block, or orchard?
- What harvest volume should we expect this season?
- Which areas need field attention or a manual check?
- How should labor, harvest schedules, packing, and buyer commitments be planned?

The product should always communicate that results are a **visible fruit-count estimate**, not a guaranteed total fruit count. Fruit hidden by leaves, branches, and canopy structure cannot always be observed from aerial imagery.

## Product promise

The mature experience should feel like this:

> Select an orchard block, press Scan, receive a harvest estimate and orchard map.

The farm should not need to become a drone company. The system must progressively remove operational complexity through:

- Predefined scan paths for registered orchard blocks
- Simple, guided flight setup and checklists
- Automatic image-quality checks
- Safe return-to-home behavior and battery safeguards
- Clear scan status and report delivery
- Remote support and a technician fallback during early deployments

This is best described initially as **supervised autonomy**. Full self-service operation is a later product milestone, earned through repeated field reliability.

## Business model: phased rollout

### Phase 1: Operator-led scan service

We visit or coordinate scans, operate the drone, process the imagery, and deliver a report/dashboard result. This is the fastest way to learn from real orchards while building the training dataset and proving accuracy.

Revenue options:

- Per scan or per orchard/block fee
- Seasonal scan package with a fixed number of visits
- Custom project contracts for co-ops, LGUs, universities, and research farms

Illustrative starting ranges, to validate with customers rather than treat as fixed prices:

- Small demonstration or pilot: PHP 1,500 to PHP 3,000
- Orchard/block scan: PHP 5,000 to PHP 15,000
- Larger cooperative, institutional, or custom monitoring project: PHP 20,000+

The purpose of Phase 1 is not simply revenue. It is to validate demand, learn operational costs, gather local data, and identify which decisions customers actually use the results for.

### Phase 2: Managed hardware subscription

Qualified commercial farms receive a configured drone system after installation and training. The company still manages flight templates, data processing, support, maintenance, and quality control.

The customer has access to the system, but the company remains responsible for the result.

Possible charging structure:

- One-time onboarding, installation, and orchard-mapping fee
- Monthly managed-service fee
- Per completed scan, per hectare, per tree, or seasonal usage fee
- Deposit or damage terms for hardware placed on-site

This phase solves the scale problem: the company does not need to physically operate every scan, while it retains enough control to protect data quality and customer trust.

### Phase 3: Self-service hardware and software

After the workflow is reliable for ordinary farm technicians, offer:

- Hardware purchase with a support and software contract
- Hardware rental or lease with maintenance
- Software subscription for scan planning, reports, history, and alerts
- Optional premium support and manual review

The software subscription is justified only when it provides continuing value, such as historical comparisons, yield trends, map-based reports, workflow planning, and management visibility. A one-time fruit count is a report, not yet a recurring software product.

## Hardware sales and rental

Selling or renting hardware is possible, but it should not be the first business model.

Early risks include crashes, poor charging practices, lost connectivity, inconsistent image capture, and customers blaming the system when an untrained operator produces bad data. These risks can destroy trust before the product is mature.

For early customers, prefer managed access over an unrestricted rental. A customer may eventually rent or lease the system, but only after onboarding, installation, basic training, and a support agreement.

The rough price idea of PHP 20,000 for two months and PHP 10,000 for each following month should not be finalized from drone build cost alone. The price must cover:

- Hardware depreciation and replacement reserve
- Repairs, batteries, and transport
- Installation and orchard flight setup
- Training and customer support
- Cloud processing and data storage
- Insurance, compliance, and operational risk
- The value of the farm decision being improved

If PHP 20,000 is close to the true build cost of a drone, renting it for PHP 20,000 over two months may be too low once support and failure risk are included. Treat that as an initial hypothesis to test with commercial farms, not a published price.

## Research strategy and intellectual property

Research is valuable, but the company should not give away its future in exchange for validation.

Use universities, DA/LGU offices, and research farms as one or more of the following:

- Pilot and validation partners
- Grant and equipment-funding partners
- Dataset and domain-expertise contributors
- Reference customers
- Publication partners, where publication does not expose critical proprietary methods prematurely

Before sharing technology, document ownership in writing. Agreements should address:

- Ownership of existing software, models, and drone workflows
- Rights to images, orchard data, and labels
- Ownership of improvements made during a study
- Confidentiality and publication review
- Commercialization rights and exclusivity, if any

The preferred relationship is: research validates and strengthens the company; the company retains its core platform and commercial rights.

## Research automation offering

There is a second customer segment alongside commercial farms: researchers, universities, agricultural offices, and crop-development programs that need repeated, structured observations of plants.

The offer should not be framed only as "we sell automation." A clearer offer is:

> We design and operate repeatable plant-monitoring workflows that collect, organize, and analyze field data for your research project.

Depending on the study, the system may track trees, fruits, vegetables, hydroponic towers, plant height, canopy condition, visible fruit counts, growth over time, or image records linked to a plant, plot, or treatment group.

The valuable deliverable is a dependable research workflow:

- A monitoring plan for the study area, plant groups, and observation schedule
- Drone, camera, fixed-camera, or manual-assisted data capture as appropriate
- Consistent IDs for plants, plots, treatments, and observation dates
- A database and dashboard showing observations over time
- Exportable images, measurements, and CSV data for research analysis
- Data-quality checks and a documented method that can be repeated

This can be sold as a project-based **Research Monitoring System** or **Plant Phenotyping Automation Service**. The term "phenotyping" may be useful with researchers, but plain language should be used with non-technical partners.

### Why it is attractive

- Research budgets may support pilots, equipment, and custom workflow development.
- Projects create high-quality labeled data and expert feedback.
- The same data platform can later support farm products.
- A controlled research site is often easier than an unmanaged commercial orchard, making it a good place to validate new sensing methods.

### The important boundary

Do not accept every custom tracking request as a one-off software project. That can turn the company into a low-margin development shop with no reusable product.

Use a productized structure:

- One-time study setup fee for defining the workflow, identifiers, database, and dashboard
- Monitoring fee per visit, scan, month, plot, or season
- Optional hardware rental or installation fee
- Optional custom-analysis fee for genuinely new measurements or models
- Clear scope for support, revisions, ownership, and data delivery

Choose research projects that reuse at least one core capability: image capture, plant/plot mapping, repeat monitoring, computer-vision measurement, or dashboard reporting. A project is strategically strong when it leaves the company with a reusable module, improved model, or new customer segment.

## Expansion strategy

Do not expand from citrus to all fruits, vegetables, and hydroponics merely because the underlying technology appears transferable. Each crop changes the vision problem, field workflow, value proposition, and sales cycle.

Expansion should follow evidence:

1. Prove a paid citrus use case.
2. Build a reliable citrus dataset and operating playbook.
3. Identify the next crop with similar image conditions and a clear economic decision.
4. Run paid pilots before building a generic multi-crop platform.

Hydroponic towers may become a separate, promising product line because the setting is more controlled and scanning can be easier. It should be treated as a focused adjacent product, not an automatic extension of the orchard business.

## Geographic strategy

Do not prioritize overseas expansion before proving local repeatability. The local advantage is precisely the Perante orange dataset, farm relationships, and operational knowledge that larger foreign companies may not have.

Build local proof first. International expansion becomes credible when the company can show:

- Repeat paid use by farms
- Measured accuracy and useful business outcomes
- A scalable operating model
- Low support burden per deployment
- A product that transfers to another crop or region with limited customization

## What would make the model fail?

The company is not likely to fail because farmers are incapable of using drones. It will struggle if it asks customers to change too much behavior before delivering enough economic value.

The most dangerous assumptions to test early are:

- Farms will pay for an estimate, not just find it interesting
- The estimate changes a real decision about labor, harvest, packing, or sales
- Scans can be completed safely and consistently in real orchard conditions
- A trained farm technician can collect usable data without the founders being on-site
- Support, travel, processing, and repairs leave enough margin

The strategic answer is a controlled progression: prove the service, manage the hardware, then enable self-service. This is a path to scale, not a sign that the product is weak.

## Near-term decisions

1. Define the first target customer as a commercial orchard, cooperative, or institution with a designated technician.
2. Design one paid pilot offer with a clear report and stated business use.
3. Measure the real cost and time of completing each scan.
4. Test whether the customer will pay for repeat seasonal monitoring.
5. Build the drone workflow so an operator can eventually succeed with guided, supervised autonomy.
