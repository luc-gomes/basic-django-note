
from rest_framework.decorators import api_view
from rest_framework.response import response
from .srializers import NoteSerializer
from .models import Note

@api_view('GET',)
# Create your views here.

def getRoutes(request):

    routes = [
        {
            'endpoint' : '/notes/',
            'method': 'GET',
            'body': None,
            'description' : 'Returns an array of notes '
        },
        {
            'Endpoint' : '/notes/id',
            'methods' : 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {   'endpoint': '/notes/create/',
            'method': 'POST',
            'body' : { 'body' : ""},
            'description': 'creates new note with data sent in post req'
        },
        {
            'endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete and existing note'
        },
    ]
    return JsonResponse(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.get()
    serializer = NoteSerializer(notes, many =True)
    return response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id = pk):
    serializer = NoteSerializer(note, many=False)
    return response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data

    note = note.objects.create(
        body=data['body']

    )
    serializer = NoteSerializer(note, many=False)
    return response(serializer)


@api_view(['PUT'])
def updateNote(request):
    data = request.data

    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.POST)
    if serializer.is_valid():
        serializer.save()
    return response(serializer)
