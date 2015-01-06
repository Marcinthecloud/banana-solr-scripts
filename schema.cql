CREATE KEYSPACE bananas WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': '1'
};

CREATE TABLE bananas.bananas_by_time (
  tree_id int,
  time timestamp,
  banana_type text,
  solr_query text,
  yield int,
  PRIMARY KEY ((tree_id), time)
);
