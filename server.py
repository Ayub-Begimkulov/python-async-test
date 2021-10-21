from multiply_string import get_task_if_finished, create_task
from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/task')
async def index(request):
    id = int(request.rel_url.query.get('id'))
    
    if id is None:
      return web.json_response(data="Id must be passed")
    
    result = get_task_if_finished(id)

    if result == 'not_ready':
      return web.json_response(data="not ready boy")
    
    return web.json_response(data=result)

@routes.post('/task')
async def create(request):
  json = await request.json()
  text = json['text']
  id = create_task(text)
  return web.json_response(data=id)


app = web.Application()
app.add_routes(routes)
web.run_app(app, port=3000)
