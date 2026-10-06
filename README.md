# 1st-project
Documenting my progression learning Python and physics programming, building toward gravitational wave data analysis skills.


# Project 1: Projectile Motion Simulator
A physics simulation project exploring projectile motion using both exact kinematics and numerical methods.
## What this project covers
- Exact trajectory calculation using standard kinematics equations 
- Comparison of different launch angles (including verifying that complementary angles, e.g. 30°/60°, give equal range)
- Euler's method: simulating motion step-by-step instead of using a  closed-form formula, and comparing its accuracy against the exact  solution at different step sizes (dt), also noted that increasing dt leads to increase in error
- Adding air resistance (quadratic drag) — a case where no exact formula exists, so numerical simulation becomes necessary rather than optional, which happens in real world
## What I learned
- How numerical integration (Euler's method) approximates continuous motion, and how step size affects accuracy
- How drag forces are modeled and why they require numerical methods
- Practical Python: NumPy arrays, Matplotlib plotting, functions, loops


# Project 2: Exoplanet Dataset Analysis
Exploring real observational data from the NASA Exoplanet Archive (Planetary Systems table), moving from self-generated data to real, messy astronomical data.

### Analysis 1: Discovery Methods Over Time
Explored how the method used to discover exoplanets has changed since the first confirmed detections in the early 1990s, using a grouped/stacked bar chart of discoveries by year and discovery method.

**Findings:**
- Early discoveries (1990s–2000s) were dominated by the Radial Velocity method, which detects planets via the gravitational wobble they cause in their host star.
- Two dramatic spikes appear in 2014 and 2016, both dominated by the Transit method — these correspond to large batches of Kepler mission candidates being confirmed and released in those years, not a sudden natural change in detection rates.
- From 2014 onward, Transit has remained the dominant discovery method by a wide margin, reflecting the impact of dedicated transit-survey missions (Kepler, later TESS) on the field.

This was a good first exercise in `pandas.groupby()` and reshaping data with `.unstack()` for a stacked bar chart — and a reminder that spikes in a dataset often reflect real-world events (a mission's data release) rather than being artifacts or errors.


### Analysis 2: Orbital Period vs Planet Mass
Investigated whether planets with longer orbital periods tend to be more massive. A scatter plot (log-log scale, due to the huge range of both variables) showed no clear pattern — confirmed numerically with a Pearson correlation coefficient of just 0.01, indicating essentially no linear relationship.
Colored the same plot by discovery method to check whether detection bias was hiding a relationship — it wasn't; each method's points spanned a wide range of masses regardless of period. This makes physical sense: unlike orbital period and distance (linked directly via Kepler's third law), planet mass and orbital period aren't governed by a shared physical relationship — mass depends on formation history, while period depends on distance from the star.


### Analysis 3: Verifying Kepler's Third Law
Plotted orbital period vs. orbital distance (semi-major axis) on a log-log scale, expecting a straight line per Kepler's third law (T² ∝ a³, meaning a log-log slope of 1.5). The data showed a clear linear relationship, and fitting a line gave a slope of 1.465 — within ~2% of the theoretical value, a strong empirical confirmation. The small deviation is expected given real measurement uncertainty and the approximation that stellar mass dominates each system.



### Analysis 4: Planet Density and Composition Proxy
Since this dataset lacks direct atmospheric/chemical composition data, computed a relative density proxy (mass ÷ radius³, in Earth units) as a stand-in for distinguishing rocky vs. gas-giant planets.

A simple histogram of density alone didn't show a clean bimodal split — instead a single skewed peak, likely because many known gas giants are "hot Jupiters" with large radii close to their star, giving them lower relative density than a naive rocky/gas split would suggest.

Plotting mass vs. radius directly, colored by density, revealed clearer structure: a distinct population of large-radius, low-density planets (gas giants), and a separate track of smaller, higher-density planets (likely rocky). This mirrors the real "radius valley" phenomenon studied in exoplanet science — a relative scarcity of planets at intermediate sizes, thought to separate rocky super-Earths from gas-enveloped mini-Neptunes.

### Analysis 5: 
initially attempted labelling using radius alone (rocky< 2 Earth radii, gas giant >6), but recognised this was a weak proxy-a planet could be physically large while still being rocky. Switched to density based labelling instead (mass/radius^3), using solar system planets as refernce points to set thresholds.

## First ML model: Decision tree classifier

Trained a decision tree (max depth 3) to classify planets as rocky or gas giant using only mass and radius as inputs. Achieved 96.96% accuracy, but recognized this is expected rather than impressive: the labels were created directly from computed density (mass/radius³), and the tree essentially rediscovered this relationship through combinations of raw mass/radius splits (visible in the tree structure) rather than learning a genuinely hidden pattern. A meaningful next step would be a harder task the model can't simply reverse-engineer from the inputs.

### Second ML model: Predicting discovery method

Unlike the rocky/gas-giant model (which could trivially reconstruct a density formula from its own inputs), predicting discovery method from mass, radius, and orbital period has no such shortcut — there's no formula linking these properties to detection method.

After balancing the dataset (98 examples each of Transit and Radial Velocity, since the raw data was ~34:1 imbalanced), a decision tree 
achieved 65% accuracy — notably better than the ~50% expected from random guessing on a balanced set, but far from perfect. This suggests a real but noisy relationship, consistent with Analysis 2's finding that Transit tends to favor shorter orbital periods while Radial Velocity tends to favor more massive planets — real detection biases, not a clean deterministic rule.

### Improving planet classifier 
Tried to make the planet classifier more realistic by using different inputs (instead of mass+radius). Testing if model can guess composition from indirect clues, the way a real astronomer sometimes has to when direct density isnt measurable.

Surprisingly, distance from Earth was the single most important feature in this tree — but this likely reflects detection bias rather than any real physical relationship. Smaller, rocky planets produce fainter detection signals and are harder to find at greater distances, so "distance" may actually be acting as a proxy for "how hard this planet was to detect" rather than directly influencing composition. This is a good example of why strong model performance doesn't automatically mean a causal relationship was found — correlation and detection bias can produce similar-looking patterns.


# Project 3: Gravitational Wave Detection (GWOSC)

First hands-on work with real LIGO data, using the GWpy library to load and analyze strain data from GW150914 — the first gravitational wave ever detected.

Note: 'Timseries.fetch_open_data()' repeatedly timed out on my network, so i downloaded the H1 strain data file manually from GWOSC's website and loaded it locally instead. The underlying data is identical either way, this was a workaround for a local network issue, not a change in the actual analysis