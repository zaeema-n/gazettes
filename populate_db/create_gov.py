import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from neo4j_util.neo4j_interface import Neo4jInterface

# Initialize Neo4j interface
neo4j_interface = Neo4jInterface()

def create_government_node():
    query = """
    MERGE (g:government {id: $id})
    SET g.name = $name
    RETURN g
    """
    params = {"id": "gov_01", "name": "Government of Sri Lanka"}
    result = neo4j_interface.execute_query(query, params)
    return result

# Create the government node
gov_node = create_government_node()
print(gov_node)
