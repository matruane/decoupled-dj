<template>
  <div class="container">
    <h2>Create a new invoice</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form">
        <div class="form__aside">
          <div class="form__field">
            <label for="user">Select a client</label>
            <select name="user" id="user" required>
              <option value="--">--</option>
              <option v-for="user in users" :key="user.email" :value="user.id">
                {{ user.name }} - {{ user.email }}
              </option>
            </select>
          </div>
          <div class="form__field">
            <label for="date">Date</label>
            <input type="date" name="date" id="date" required />
          </div>
          <div class="form__field">
            <label for="due_date">Due date</label>
            <input type="date" name="due_date" id="due_date" required />
          </div>
        </div>
        <div class="form__main">
          <div class="form__feild">
            <label for="quantity">Qty</label>
            <input
              type="number"
              id="quantity"
              name="quantity"
              min="0"
              max="10"
              required
            />
          </div>
          <div class="form__feild">
            <label for="description">Description</label>
            <input type="text" id="description" name="description" required />
          </div>
          <div class="form__feild">
            <label for="price">Price</label>
            <input 
              type="number"
              id="price"
              name="price"
              min="0"
              step="0.01"
              required
            />
          </div>
          <div class="form__feild">
            <label for="taxed">Taxed</label>
            <input type="checkbox" id="taxed" name="taxed" required />
          </div>
        </div>
      </div>
      <div class="form__buttons">
        <button type="submit">Create invoice</button>
        <button disabled>Send email</button>
      </div>
    </form>
  </div>
</template>

<script>
  export default {
    name: "InvoiceCreate",
    data: () => ({
      users: [
        { id: 1, name: "Bert", email: "bert@example.com" },
        { id: 2, name: "Ernie", email: "ernie@example.com" }
      ]
    }),
    methods: {
      handleSubmit: (e) => {
        // eslint-disable-next-line
        const formData = new FormData(e.target);

        const data = {};

        fetch("/billing/api/invoices/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data)
        })
        .then(response => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then(json => {
          console.log(json);
        })
        .catch(err => console.error(err))
      },
      mounted: () => {
        fetch("/billing/api/clients/")
        .then(response => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then(json => {
          this.users = json;
        })
      }
    }
  };
</script>
