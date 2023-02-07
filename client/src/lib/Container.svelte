<script>
    let toDoItems = [1,2,3,4,5];
</script>
{#each toDoItems as todoItem}
    <div class="row">
        <div class="col s12 m6">
            <div class="card">
                <span class="card-title" style="color: black">Card Title</span>
                <div class="card-content">
                    <p style="color: black">I am a very simple card. I am good at containing small bits of information. I am
                        convenient because I require little markup to use effectively.</p>
                </div>
            </div>
        </div>
    </div>
{/each}