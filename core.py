import gym
from gym import spaces

class Env(gym.Env):
    """Base class capable of handling vectorized environments.
    """
    metadata = {
        # This key indicates whether an env is vectorized (or, in the case of
        # Wrappers where autovectorize=True, whether they should automatically
        # be wrapped by a Vectorize wrapper.)
        'runtime.vectorized': True,
    }

    # Number of remotes. User should set this.
    n = None


class Wrapper(Env, gym.Wrapper):
    """Use this instead of gym.Wrapper iff you're wrapping a vectorized env,
    (or a vanilla env you wish to be vectorized).
    """
    # If True and this is instantiated with a non-vectorized environment,
    # automatically wrap it with the Vectorize wrapper.
    autovectorize = True

    def __init__(self, env):
        super(Wrapper, self).__init__(env)
        if not env.metadata.get('runtime.vectorized'):
            if self.autovectorize:
                # Circular dependency :(
                from universe import wrappers
                env = wrappers.Vectorize(env)
            else:
                raise Exception('This wrapper can only wrap vectorized envs (i.e. where env.metadata["runtime.vectorized"] = True), not {}. Set "self.autovectorize = True" to automatically add a Vectorize wrapper.'.format(env))

        self.env = env

    @property
    def n(self):
        return self.env.n

    def configure(self, **kwargs):
        self.env.configure(**kwargs)

class ObservationWrapper(Wrapper, gym.ObservationWrapper):
    pass

class RewardWrapper(Wrapper, gym.RewardWrapper):
    pass

class ActionWrapper(Wrapper, gym.ActionWrapper):
    pass
