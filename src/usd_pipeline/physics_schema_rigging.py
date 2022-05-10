class PhysicsSchemaRigging:
    """
    Applies UsdPhysics rigid body, collision APIs, and revolute joints
    to OpenUSD mechanical assemblies.
    """
    @staticmethod
    def apply_revolute_joint(prim_path: str, axis: str = "Z", lower_limit: float = -180.0, upper_limit: float = 180.0):
        return {
            "prim": prim_path,
            "physics:axis": axis,
            "physics:lowerLimit": lower_limit,
            "physics:upperLimit": upper_limit
        }
