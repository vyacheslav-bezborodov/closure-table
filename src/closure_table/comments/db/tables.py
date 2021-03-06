import sqlalchemy as sa

meta = sa.MetaData()

comments = sa.Table(
    'comments_comments', meta,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('content', sa.String, nullable=False),
)

comments_tree = sa.Table(
    'comments_tree', meta,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('ancestor_id', sa.Integer, sa.ForeignKey(comments.c.id), nullable=False),
    sa.Column('nearest_ancestor_id', sa.Integer, sa.ForeignKey(comments.c.id), nullable=False),
    sa.Column('descendant_id', sa.Integer, sa.ForeignKey(comments.c.id), nullable=False),
    sa.Column('depth', sa.Integer, nullable=False),
)
