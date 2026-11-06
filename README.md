# gauntlet-demo

The demo task repository for [Gauntlet](https://github.com/ShivVIT2019/gauntlet), our Flip the Switch Hackathon project.

`rate_limiter.py` contains two intentional bugs, and `test_rate_limiter.py` holds the five tests the agents must pass. **Do not merge PRs into `main`**: the bugs must stay so every race starts from the same code.

- `agent-cheat`: a prepared branch that passes only by weakening its tests, used to show cheat detection
- `replay-*`: saved results from a real three-vendor race, used by `gauntlet.py replay`

See the [Gauntlet README](https://github.com/ShivVIT2019/gauntlet) for how it works and how to run it.
