from neomodel import config,StringProperty, StructuredNode, RelationshipTo, RelationshipFrom, Relationship,db,UniqueIdProperty,IntegerProperty
import pprint
from textwrap import dedent

config.DATABASE_URL = 'bolt://neo4j:12345678@localhost:7687'

class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)
    # name = StringProperty(unique_index=True, required=True)



class City(StructuredNode):
    name = StringProperty(required=True)
    country = RelationshipTo(Country, 'FROM_COUNTRY')

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)
    country = RelationshipTo(Country, 'IS_FROM')
    city = RelationshipTo(City, 'LIVES_IN')



def test_connect():
    result,meta = db.cypher_query("RETURN 'Hello World' as message")
    print(pprint.pformat(result))

    # 匹配任意节点，返回任意节点
    result, meta = db.cypher_query("MATCH (n) RETURN n")
    print(pprint.pformat(result))

    expr = dedent("""
    MATCH (ee:Person)-[:KNOWS]->(friends)
    WHERE ee.name = 'Songzj' Return ee,friends
    """)

    result,meta = db.cypher_query(expr)
    print(pprint.pformat(result))


def test_crud():
    jim = Person(name='Jim', age=3).save()
    jim.age = 4
    jim.save()

    print(jim.element_id)

    all_nodes = Person.nodes.all()
    print(all_nodes)

    jim2 = Person.nodes.filter(name='Jim')
    print(jim2)


def test_edge():
    jim = Person(name='Songzj', age=3).save()

    germany = Country(code='DE').save()
    jim.country.connect(germany)
    berlin = City(name='Berlin').save()
    berlin.country.connect(germany)
    jim.city.connect(berlin)
    germany.save()
    berlin.save()

    jim.save()

