from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams


def build_pains_catalog():
    """Build an RDKit PAINS filter catalog."""
    params = FilterCatalogParams()
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS_A)
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS_B)
    params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS_C)
    return FilterCatalog(params)


def get_pains_matches(mol, catalog=None):
    """Return PAINS alert names for a molecule."""
    if mol is None:
        return []

    if catalog is None:
        catalog = build_pains_catalog()

    matches = catalog.GetMatches(mol)
    return [match.GetDescription() for match in matches]


def has_pains_alert(mol, catalog=None):
    """Return True if a molecule has at least one PAINS alert."""
    return len(get_pains_matches(mol, catalog)) > 0
